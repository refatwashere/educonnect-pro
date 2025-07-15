# EduConnect Pro

A free, open-source educational institution management platform with real database integration.

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** and **pip**
- **Node.js 18+** and **pnpm**
- **Git**

### Development Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd educonnect-pro
   ```

2. **Start development servers**:
   ```bash
   # Windows
   scripts\start-dev.bat
   
   # Linux/Mac
   scripts/start-dev.sh
   ```

3. **Access the application**:
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs

### Default Login
- **Username**: `teacher@school.edu`
- **Password**: `password`

## 🗄️ Database Integration

### Development (SQLite)
- **Auto-setup**: Database created automatically on first run
- **No config needed**: Works out of the box
- **Perfect for**: Local development and testing

### Production (Supabase PostgreSQL)
- **Free tier**: 500MB PostgreSQL database
- **Setup**: Create Supabase project and update `DATABASE_URL`
- **Features**: Real-time, built-in auth, REST API
- **Guide**: See [Database Setup](./docs/database-setup.md)

## ✨ Current Features

- 🏫 **Class Management** - Full CRUD with database persistence
- 👥 **User Authentication** - Secure JWT-based login system
- 🗄️ **Database Integration** - SQLite (dev) + PostgreSQL (prod)
- 📊 **API Documentation** - Interactive Swagger UI
- 🔒 **Type Safety** - Shared TypeScript types
- 📱 **Responsive Design** - Mobile-friendly interface
- 🚀 **Auto-setup** - One-command development start

## 🏗️ Architecture

```
educonnect-pro/
├── backend/                 # FastAPI + SQLAlchemy
│   ├── src/
│   │   ├── models/         # Database models
│   │   ├── routes/         # API endpoints
│   │   ├── services/       # Business logic
│   │   └── config/         # Database & settings
│   └── requirements.txt    # Python dependencies
├── frontend/               # Next.js + TypeScript
│   ├── src/app/           # App router pages
│   └── package.json       # Node.js dependencies
├── shared/                 # Shared TypeScript types
├── scripts/               # Development automation
└── docs/                  # Comprehensive documentation
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pip install pytest pytest-asyncio httpx
pytest
```

### API Testing
```bash
# Login test
curl -X POST "http://localhost:8000/api/v3/auth/token" \
  -d "username=teacher@school.edu&password=password"

# Classes test
curl -X GET "http://localhost:8000/api/v3/classes" \
  -H "Authorization: Bearer <token>"
```

## 📚 Documentation

Comprehensive guides available in [`docs/`](./docs/):

- **[Getting Started](./docs/getting-started.md)** - Setup and installation
- **[Database Setup](./docs/database-setup.md)** - SQLite and Supabase configuration
- **[API Guide](./docs/api-guide.md)** - Backend API reference
- **[Frontend Guide](./docs/frontend-guide.md)** - UI development
- **[Testing Guide](./docs/testing-guide.md)** - Testing setup and examples
- **[Next Steps](./docs/next-steps.md)** - Development roadmap
- **[Deployment](./docs/deployment.md)** - Production deployment
- **[Troubleshooting](./docs/troubleshooting.md)** - Common issues

## 🎯 Next Steps

### Immediate (Week 1-2)
- [ ] Set up Supabase PostgreSQL for production
- [ ] Add comprehensive test suite
- [ ] Create class management forms
- [ ] Implement edit/delete functionality

### Short-term (Month 1)
- [ ] Student management system
- [ ] Enhanced authentication (refresh tokens)
- [ ] Dashboard with analytics
- [ ] Mobile app considerations

### Long-term (Month 2+)
- [ ] Timetable generation
- [ ] Reporting system
- [ ] Real-time notifications
- [ ] Advanced user roles

See [Next Steps Guide](./docs/next-steps.md) for detailed roadmap.

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Database ORM
- **PostgreSQL/SQLite** - Database options
- **JWT** - Authentication
- **Pydantic** - Data validation

### Frontend
- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Shared Types** - Frontend-backend communication

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Make changes and test thoroughly
4. Submit pull request

See [Contributing Guide](./docs/contributing.md) for details.

## 📄 License

Open source under the [MIT License](LICENSE).

## 🆘 Support

- 📖 [Documentation](./docs/)
- 🐛 [GitHub Issues](../../issues)
- 💬 [Discussions](../../discussions)

---

**EduConnect Pro** - Making education management accessible with modern technology.
