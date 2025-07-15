# Contributing to EduConnect Pro

Thank you for your interest in contributing to EduConnect Pro! This guide will help you get started.

## Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/educonnect-pro.git
   cd educonnect-pro
   ```
3. **Follow the [Getting Started Guide](./getting-started.md)** to set up your development environment

## Making Changes

### Backend Changes

1. Navigate to the backend directory:
   ```bash
   cd backend
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

2. Make your changes to the FastAPI application

3. Test your changes:
   ```bash
   uvicorn src.main:app --reload
   ```

### Frontend Changes

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Make your changes to the Next.js application

3. Test your changes:
   ```bash
   pnpm dev
   ```

## Code Style

### Backend (Python)

- Follow PEP 8 style guidelines
- Use type hints where possible
- Add docstrings to functions and classes
- Keep functions focused and small

Example:
```python
from typing import List, Optional

async def get_classes(user_id: str) -> List[Class]:
    """
    Retrieve all classes for a specific user.
    
    Args:
        user_id: The ID of the user
        
    Returns:
        List of Class objects
    """
    # Implementation here
```

### Frontend (TypeScript/React)

- Use TypeScript for type safety
- Follow React best practices
- Use functional components with hooks
- Keep components small and focused

Example:
```tsx
interface ClassCardProps {
  class: Class;
  onEdit: (id: string) => void;
}

export function ClassCard({ class: cls, onEdit }: ClassCardProps) {
  return (
    <div className="p-4 border rounded">
      <h3 className="font-semibold">{cls.name}</h3>
      <p className="text-gray-600">{cls.description}</p>
      <button onClick={() => onEdit(cls.id)}>Edit</button>
    </div>
  );
}
```

## Testing

### Backend Testing

```bash
cd backend
# Add tests in tests/ directory
pytest
```

### Frontend Testing

```bash
cd frontend
# Add tests alongside components
pnpm test
```

## Submitting Changes

1. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and commit them:
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

3. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request** on GitHub

## Pull Request Guidelines

- **Clear title** describing the change
- **Detailed description** of what was changed and why
- **Link to any related issues**
- **Screenshots** for UI changes
- **Test your changes** before submitting

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## Testing
- [ ] Backend tests pass
- [ ] Frontend tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots here
```

## Issue Reporting

When reporting bugs or requesting features:

1. **Search existing issues** first
2. **Use the issue templates** provided
3. **Include detailed information**:
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details
   - Screenshots/logs if applicable

## Development Guidelines

### API Development

- Follow RESTful conventions
- Use proper HTTP status codes
- Include comprehensive error handling
- Document endpoints with OpenAPI/Swagger

### UI Development

- Follow accessibility guidelines (WCAG)
- Ensure responsive design
- Use semantic HTML
- Test with keyboard navigation

### Database Changes

- Create migration scripts
- Test with sample data
- Consider backward compatibility

## Getting Help

- Check the [Troubleshooting Guide](./troubleshooting.md)
- Ask questions in GitHub Discussions
- Join our community chat (if available)

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to EduConnect Pro!