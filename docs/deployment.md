# Deployment Guide

This guide covers deploying EduConnect Pro to production environments.

## Prerequisites

- **Domain name** (optional but recommended)
- **SSL certificate** (Let's Encrypt recommended)
- **Server** with Docker support or Python/Node.js runtime
- **Database** (PostgreSQL recommended for production)

## Production Environment Setup

### Option 1: Docker Deployment (Recommended)

Create `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/educonnect
      - SECRET_KEY=your-production-secret-key
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=https://your-domain.com/api

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=educonnect
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - backend
      - frontend

volumes:
  postgres_data:
```

### Option 2: Manual Deployment

#### Backend Deployment

1. **Prepare the server**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv postgresql
   ```

2. **Clone and setup**:
   ```bash
   git clone <repository-url>
   cd educonnect-pro/backend
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with production values
   ```

4. **Run with Gunicorn**:
   ```bash
   pip install gunicorn
   gunicorn src.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
   ```

#### Frontend Deployment

1. **Build the application**:
   ```bash
   cd frontend
   pnpm install
   pnpm build
   ```

2. **Serve with PM2**:
   ```bash
   npm install -g pm2
   pm2 start npm --name "educonnect-frontend" -- start
   ```

## Environment Variables

### Backend (.env)

```bash
# Security
SECRET_KEY=your-super-secret-production-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/educonnect

# CORS
CORS_ORIGINS=https://your-domain.com,https://www.your-domain.com

# Optional
DEBUG=false
LOG_LEVEL=info
```

### Frontend (.env.local)

```bash
NEXT_PUBLIC_API_URL=https://your-domain.com/api
NEXT_PUBLIC_APP_NAME=EduConnect Pro
```

## Database Setup

### PostgreSQL Setup

1. **Install PostgreSQL**:
   ```bash
   sudo apt install postgresql postgresql-contrib
   ```

2. **Create database and user**:
   ```sql
   sudo -u postgres psql
   CREATE DATABASE educonnect;
   CREATE USER educonnect_user WITH PASSWORD 'secure_password';
   GRANT ALL PRIVILEGES ON DATABASE educonnect TO educonnect_user;
   \q
   ```

3. **Run migrations** (when implemented):
   ```bash
   python manage.py migrate
   ```

## Nginx Configuration

Create `/etc/nginx/sites-available/educonnect`:

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com www.your-domain.com;

    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

    # Frontend
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## SSL Certificate (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

## Process Management

### Systemd Service (Backend)

Create `/etc/systemd/system/educonnect-backend.service`:

```ini
[Unit]
Description=EduConnect Pro Backend
After=network.target

[Service]
Type=exec
User=www-data
Group=www-data
WorkingDirectory=/path/to/educonnect-pro/backend
Environment=PATH=/path/to/educonnect-pro/backend/.venv/bin
ExecStart=/path/to/educonnect-pro/backend/.venv/bin/gunicorn src.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable educonnect-backend
sudo systemctl start educonnect-backend
```

## Monitoring and Logging

### Log Configuration

Backend logging in `src/main.py`:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/educonnect/backend.log'),
        logging.StreamHandler()
    ]
)
```

### Health Checks

Add health check endpoint:
```python
@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow()}
```

## Backup Strategy

### Database Backup

```bash
#!/bin/bash
# backup-db.sh
pg_dump -h localhost -U educonnect_user educonnect > backup_$(date +%Y%m%d_%H%M%S).sql
```

### File Backup

```bash
#!/bin/bash
# backup-files.sh
tar -czf backup_files_$(date +%Y%m%d_%H%M%S).tar.gz /path/to/educonnect-pro
```

## Security Checklist

- [ ] Use HTTPS everywhere
- [ ] Set strong SECRET_KEY
- [ ] Configure CORS properly
- [ ] Use environment variables for secrets
- [ ] Enable firewall (UFW)
- [ ] Regular security updates
- [ ] Database connection encryption
- [ ] Rate limiting (consider nginx rate limiting)
- [ ] Input validation and sanitization

## Performance Optimization

### Backend

- Use connection pooling for database
- Implement caching (Redis)
- Enable gzip compression
- Use CDN for static assets

### Frontend

- Enable Next.js optimizations
- Optimize images
- Use service worker for caching
- Minimize bundle size

## Troubleshooting

### Common Issues

1. **502 Bad Gateway**: Check if backend service is running
2. **CORS errors**: Verify CORS_ORIGINS configuration
3. **Database connection**: Check DATABASE_URL and credentials
4. **SSL issues**: Verify certificate paths and permissions

### Logs Location

- Backend: `/var/log/educonnect/backend.log`
- Nginx: `/var/log/nginx/access.log`, `/var/log/nginx/error.log`
- System: `journalctl -u educonnect-backend`

## Scaling Considerations

- **Load balancing**: Use multiple backend instances
- **Database**: Consider read replicas
- **Caching**: Implement Redis for session storage
- **CDN**: Use CloudFlare or similar for static assets
- **Monitoring**: Implement application monitoring (Prometheus, Grafana)