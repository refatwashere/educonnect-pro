#!/bin/bash

echo "Running EduConnect Pro Backend Tests..."
echo

cd backend

echo "Installing test dependencies..."
pip install -r requirements.txt

echo
echo "Running tests..."
pytest -v

echo
echo "Running tests with coverage..."
pytest --cov=src tests/ --cov-report=term-missing

echo
echo "Tests completed!"