'use client';

import { useEffect, useState } from 'react';
import { Class, ClassCreate, ClassUpdate } from '../../shared/types';
import ClassForm from '../../components/ClassForm';
import ConfirmDialog from '../../components/ConfirmDialog';

export default function ClassesPage() {
  const [classes, setClasses] = useState<Class[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [editingClass, setEditingClass] = useState<Class | null>(null);
  const [formLoading, setFormLoading] = useState(false);
  const [deleteDialog, setDeleteDialog] = useState<{ isOpen: boolean; class: Class | null }>({
    isOpen: false,
    class: null
  });

  useEffect(() => {
    fetchClasses();
  }, []);

  const fetchClasses = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch('http://localhost:8000/api/v3/classes', {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      });

      if (!response.ok) {
        throw new Error('Failed to fetch classes');
      }

      const data = await response.json();
      setClasses(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateClass = async (classData: ClassCreate) => {
    setFormLoading(true);
    try {
      const token = localStorage.getItem('token');
      const response = await fetch('http://localhost:8000/api/v3/classes', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(classData)
      });

      if (!response.ok) {
        throw new Error('Failed to create class');
      }

      await fetchClasses();
      setShowForm(false);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to create class');
    } finally {
      setFormLoading(false);
    }
  };

  const handleUpdateClass = async (classData: ClassUpdate) => {
    if (!editingClass) return;
    
    setFormLoading(true);
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`http://localhost:8000/api/v3/classes/${editingClass.id}`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(classData)
      });

      if (!response.ok) {
        throw new Error('Failed to update class');
      }

      await fetchClasses();
      setEditingClass(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to update class');
    } finally {
      setFormLoading(false);
    }
  };

  const handleDeleteClass = async () => {
    if (!deleteDialog.class) return;

    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`http://localhost:8000/api/v3/classes/${deleteDialog.class.id}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });

      if (!response.ok) {
        throw new Error('Failed to delete class');
      }

      await fetchClasses();
      setDeleteDialog({ isOpen: false, class: null });
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to delete class');
    }
  };

  if (loading) {
    return (
      <div className="p-6">
        <div className="animate-pulse">Loading classes...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-6">
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          Error: {error}
        </div>
        <button 
          onClick={() => {
            setError(null);
            fetchClasses();
          }}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Retry
        </button>
      </div>
    );
  }

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-900">Classes</h1>
        <button 
          onClick={() => setShowForm(true)}
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
        >
          Add Class
        </button>
      </div>

      {classes.length === 0 ? (
        <div className="text-center py-12">
          <p className="text-gray-500 text-lg">No classes found</p>
          <p className="text-gray-400">Create your first class to get started</p>
        </div>
      ) : (
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {classes.map((cls) => (
            <div key={cls.id} className="bg-white border border-gray-200 rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
              <div className="flex justify-between items-start mb-2">
                <h2 className="text-xl font-semibold text-gray-900">{cls.name}</h2>
                <div className="flex gap-2">
                  <button
                    onClick={() => setEditingClass(cls)}
                    className="text-blue-600 hover:text-blue-800 text-sm"
                  >
                    Edit
                  </button>
                  <button
                    onClick={() => setDeleteDialog({ isOpen: true, class: cls })}
                    className="text-red-600 hover:text-red-800 text-sm"
                  >
                    Delete
                  </button>
                </div>
              </div>
              
              <p className="text-gray-600 mb-3">{cls.description || 'No description'}</p>
              
              <div className="flex justify-between items-center text-sm text-gray-500">
                <span>Subject: {cls.subject || 'N/A'}</span>
                <span>Grade: {cls.grade_level || 'N/A'}</span>
              </div>
              
              <div className="mt-3 text-sm text-gray-500">
                Students: {cls.students_count}
              </div>
            </div>
          ))}
        </div>
      )}

      {showForm && (
        <ClassForm
          onSubmit={handleCreateClass}
          onCancel={() => setShowForm(false)}
          loading={formLoading}
        />
      )}

      {editingClass && (
        <ClassForm
          initialData={editingClass}
          onSubmit={handleUpdateClass}
          onCancel={() => setEditingClass(null)}
          isEditing={true}
          loading={formLoading}
        />
      )}

      <ConfirmDialog
        isOpen={deleteDialog.isOpen}
        title="Delete Class"
        message={`Are you sure you want to delete "${deleteDialog.class?.name}"? This action cannot be undone.`}
        onConfirm={handleDeleteClass}
        onCancel={() => setDeleteDialog({ isOpen: false, class: null })}
      />
    </div>
  );
}