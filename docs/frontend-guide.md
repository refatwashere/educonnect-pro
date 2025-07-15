# Frontend Development Guide

EduConnect Pro frontend built with Next.js 14, TypeScript, and Tailwind CSS.

## Technology Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Validation**: Zod
- **Icons**: Lucide React
- **UI Components**: Radix UI

## Project Structure

```
frontend/
├── src/
│   └── app/
│       ├── globals.css      # Global styles
│       ├── layout.tsx       # Root layout
│       └── page.tsx         # Home page
├── package.json
├── tailwind.config.ts
└── tsconfig.json
```

## Development

### Start Development Server

```bash
cd frontend
pnpm dev
```

Visit: http://localhost:3000

### Available Scripts

```bash
pnpm dev      # Start development server
pnpm build    # Build for production
pnpm start    # Start production server
pnpm lint     # Run ESLint
```

## Creating Pages

### Basic Page

Create `src/app/classes/page.tsx`:

```tsx
export default function ClassesPage() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Classes</h1>
      <p>Manage your classes here.</p>
    </div>
  );
}
```

### Page with API Integration

```tsx
'use client';

import { useEffect, useState } from 'react';

interface Class {
  id: string;
  name: string;
  description: string;
}

export default function ClassesPage() {
  const [classes, setClasses] = useState<Class[]>([]);

  useEffect(() => {
    fetch('/api/v3/classes', {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    })
    .then(res => res.json())
    .then(setClasses);
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Classes</h1>
      <div className="grid gap-4">
        {classes.map(cls => (
          <div key={cls.id} className="p-4 border rounded">
            <h2 className="font-semibold">{cls.name}</h2>
            <p className="text-gray-600">{cls.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

## Styling Guidelines

### Tailwind CSS Classes

```tsx
// Layout
<div className="container mx-auto px-4">
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">

// Typography
<h1 className="text-3xl font-bold text-gray-900">
<p className="text-gray-600 leading-relaxed">

// Buttons
<button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded">

// Forms
<input className="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">
```

## State Management

Using Zustand for global state:

```tsx
// stores/auth.ts
import { create } from 'zustand';

interface AuthState {
  token: string | null;
  user: User | null;
  login: (token: string, user: User) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  token: null,
  user: null,
  login: (token, user) => set({ token, user }),
  logout: () => set({ token: null, user: null }),
}));
```

## API Integration

### Fetch with Authentication

```tsx
const token = localStorage.getItem('token');

const response = await fetch('/api/v3/classes', {
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  }
});
```

### Error Handling

```tsx
try {
  const response = await fetch('/api/v3/classes');
  if (!response.ok) {
    throw new Error('Failed to fetch classes');
  }
  const classes = await response.json();
  setClasses(classes);
} catch (error) {
  console.error('Error:', error);
  // Handle error (show toast, etc.)
}
```

## Best Practices

1. **Use TypeScript** for type safety
2. **Component composition** over inheritance
3. **Server components** when possible
4. **Client components** only when needed
5. **Responsive design** with Tailwind
6. **Accessibility** with proper ARIA labels
7. **Error boundaries** for error handling