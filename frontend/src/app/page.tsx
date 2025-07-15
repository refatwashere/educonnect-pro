import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-16">
        <div className="text-center mb-16">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Welcome to EduConnect Pro
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Free, open-source educational institution management platform
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-4xl mx-auto">
          <Link
            href="/login"
            className="group bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow border border-gray-200"
          >
            <h2 className="text-xl font-semibold text-gray-900 mb-3 group-hover:text-blue-600">
              Login →
            </h2>
            <p className="text-gray-600">
              Sign in to access your dashboard and manage classes
            </p>
          </Link>

          <Link
            href="/classes"
            className="group bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow border border-gray-200"
          >
            <h2 className="text-xl font-semibold text-gray-900 mb-3 group-hover:text-blue-600">
              Classes →
            </h2>
            <p className="text-gray-600">
              View and manage all classes in your institution
            </p>
          </Link>

          <a
            href="http://localhost:8000/docs"
            target="_blank"
            rel="noopener noreferrer"
            className="group bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow border border-gray-200"
          >
            <h2 className="text-xl font-semibold text-gray-900 mb-3 group-hover:text-blue-600">
              API Docs →
            </h2>
            <p className="text-gray-600">
              Explore the interactive API documentation
            </p>
          </a>
        </div>

        <div className="mt-16 text-center">
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-6 max-w-2xl mx-auto">
            <h3 className="text-lg font-semibold text-blue-900 mb-2">
              Default Login Credentials
            </h3>
            <p className="text-blue-700">
              Username: <code className="bg-blue-100 px-2 py-1 rounded">teacher@school.edu</code>
            </p>
            <p className="text-blue-700">
              Password: <code className="bg-blue-100 px-2 py-1 rounded">password</code>
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}