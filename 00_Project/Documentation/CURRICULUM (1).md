# CURRICULUM

Version: 1.0

Status: Active

Project: AI Engineer Blueprint

Owner: Ahmed Ali

Last Updated: 2026-07-16

---

# Purpose

This document breaks down every phase in ROADMAP.md into a week-by-week study plan.

Each week defines:

- Topics
- Practical Exercises
- Deliverable (mini project or milestone)

This document does not replace ROADMAP.md.

ROADMAP.md defines *where we are going*.

CURRICULUM.md defines *how we get there, week by week*.

---

# Phase 0 — Environment Setup

Status: ✅ Completed

No weekly breakdown needed. Covered fully in AI_HANDOFF.md and PROGRESS.md.

---

# Phase 1 — Python Foundation

Duration: 5 Weeks

## Week 1 — Basics & Control Flow ✅ Completed

Topics

- Variables
- Data Types (int, float, str, bool)
- Operators (arithmetic, comparison, logical)
- Input / Output
- Basic Debugging in VS Code
- Conditions (if / elif / else)
- Comparison & Logical Chaining
- Loops (for, while)
- break / continue
- Nested Loops

Exercises

- Simple arithmetic scripts
- Temperature converter
- Basic user-input programs
- Number guessing game
- FizzBuzz
- Grade classifier

Deliverable

Mini Project: Simple Calculator (with error handling for division by zero and invalid operations)

---

## Week 2 — Functions & Modules ✅ Completed

Topics

- Defining Functions
- Parameters & Return Values
- Default Arguments
- Scope (local vs global)
- Importing Modules
- Organizing Code Into Files

Exercises

- Refactor Week 1–2 projects into functions
- Build a small math utilities module

Deliverable

Mini Project: Calculator (v2 — refactored using functions and modules)

---

## Week 3 — Data Structures ✅ Completed

Topics

- Lists
- Tuples
- Dictionaries
- Sets
- Common Operations & Methods
- List/Dict Comprehensions (intro level)

Exercises

- Word frequency counter
- Contact book (in-memory)
- Data filtering exercises

Deliverable

Mini Project: Expense Tracker (v1 — in-memory, no file storage yet)

---

## Week 4 — Files & Error Handling

Topics

- Reading/Writing Text Files
- Working with CSV
- Working with JSON
- try / except / finally
- Raising Custom Exceptions
- Input Validation

Exercises

- Save/load data from Week 3 projects to files
- Build a simple logging utility

Deliverable

Mini Project: Expense Tracker (v2 — persists data to a JSON/CSV file)

---

## Week 5 — OOP & Packaging

Topics

- Classes & Objects
- Attributes & Methods
- __init__ and self
- Basic Inheritance
- Organizing a Project Into Packages
- Intro to Virtual Environments (venv)

Exercises

- Convert Expense Tracker to a class-based design
- Build a small OOP-based Student model

Deliverable

Mini Project: Student Management System (v1, OOP-based)

Phase 1 Final Deliverable

Python Developer Foundation — portfolio-ready versions of:

- Calculator
- Quiz App
- Expense Tracker
- Student Management System
- Password Manager (built as a capstone exercise for the phase, combining files + OOP + error handling)

---

# Phase 2 — Software Engineering

Duration: 4 Weeks

## Week 1 — Git & GitHub Mastery

Topics

- Git Internals (staging, commits, branches)
- Branching Strategy
- Merge vs Rebase (conceptual)
- Pull Requests
- .gitignore
- Conventional Commits (deep dive)

Exercises

- Practice branching/merging on a sandbox repo
- Rewrite commit history on a test branch (safe practice)

Deliverable

Clean Git history on one existing project

---

## Week 2 — Clean Code & Design Principles

Topics

- Clean Code Fundamentals
- Naming, Functions, Comments
- SOLID Principles (introductory level)
- Code Smells
- Refactoring Techniques

Exercises

- Identify code smells in Phase 1 projects
- Refactor one project applying SOLID basics

Deliverable

Refactored version of Expense Tracker or Student Management System

---

## Week 3 — Debugging & Testing

Topics

- Debugging Tools in VS Code
- Reading Tracebacks
- Unit Testing with `unittest` or `pytest`
- Writing Testable Functions
- Test Coverage Basics

Exercises

- Write tests for existing Phase 1 functions
- Fix bugs found through testing

Deliverable

Test suite added to one existing project

---

## Week 4 — Documentation Upgrade

Topics

- Writing Professional READMEs
- Docstrings & Code Comments
- API Documentation Basics
- Project Documentation Standards (per PROJECT_RULES.md)

Exercises

- Upgrade documentation for all Phase 1 projects

Deliverable

Phase 2 Final Deliverable: Professional Engineering Skills — all Phase 1 projects refactored, tested, and documented to a professional standard

---

# Phase 3 — Backend Foundation

Duration: 5 Weeks

## Week 1 — HTTP & Web Fundamentals

Topics

- How HTTP Works
- Requests & Responses
- Status Codes
- JSON as a Data Format
- REST Principles

Exercises

- Explore public APIs using `requests`
- Build a script that consumes a public REST API

Deliverable

CLI tool that fetches and displays data from a public API

---

## Week 2 — Intro to FastAPI

Topics

- FastAPI Basics
- Routes & Path Parameters
- Query Parameters
- Request Bodies (Pydantic models)
- Automatic Docs (Swagger)

Exercises

- Build basic CRUD endpoints (in-memory storage)

Deliverable

Mini Project: Task API (v1 — in-memory)

---

## Week 3 — Databases & SQL

Topics

- Relational Database Concepts
- SQL Basics (SELECT, INSERT, UPDATE, DELETE)
- Schema Design
- Using SQLite

Exercises

- Design a schema for the Task API
- Write raw SQL queries against sample data

Deliverable

SQL schema + sample queries for Task API

---

## Week 4 — Connecting FastAPI to a Database

Topics

- SQLAlchemy Basics (or equivalent ORM)
- Connecting FastAPI to SQLite
- Migrations (basic concept)
- CRUD With Persistent Storage

Exercises

- Migrate Task API from in-memory to database-backed

Deliverable

Mini Project: Task API (v2 — persistent storage)

---

## Week 5 — Authentication & Notes API

Topics

- Authentication Concepts (API keys, tokens)
- Basic JWT Authentication in FastAPI
- Protecting Routes
- Error Handling in APIs

Exercises

- Add authentication to Task API

Deliverable

Phase 3 Final Deliverable: Notes API — full CRUD, database-backed, authenticated

---

# Phase 4 — AI Engineering Foundation

Duration: 8 Weeks

## Week 1–2 — NumPy & Data Fundamentals

Topics

- NumPy Arrays
- Vectorized Operations
- Basic Linear Algebra Operations (conceptual, no heavy math)

Exercises

- Array manipulation exercises

Deliverable

Data manipulation script using NumPy

---

## Week 3–4 — Pandas & Data Processing

Topics

- DataFrames & Series
- Reading/Cleaning Real Datasets
- Filtering, Grouping, Aggregating
- Merging Datasets

Exercises

- Clean a real-world messy dataset

Deliverable

Mini Project: Data Analysis Report on a public dataset

---

## Week 5–6 — Machine Learning Basics

Topics

- What Machine Learning Is (conceptually)
- Supervised vs Unsupervised Learning
- Using scikit-learn for a Simple Model
- Train/Test Splits
- Basic Evaluation Metrics

Exercises

- Train a simple classification or regression model

Deliverable

Mini Project: ML Mini Project (e.g., simple prediction model)

---

## Week 7–8 — AI Workflow & Integration

Topics

- End-to-End AI Workflow (data → model → output)
- Connecting an ML Model to a Simple API
- Saving/Loading Trained Models

Exercises

- Wrap the Week 5–6 model in a FastAPI endpoint

Deliverable

Phase 4 Final Deliverable: AI Fundamentals — data pipeline + trained model + API integration

---

# Phase 5 — LLM Engineering

Duration: 10 Weeks

## Week 1–2 — LLM Basics & Prompt Engineering

Topics

- How LLMs Work (conceptual, no heavy math)
- Tokens, Context Windows
- Prompt Engineering Techniques
- Using the Anthropic API

Exercises

- Build simple prompt-based scripts using the API

Deliverable

CLI tool powered by an LLM API call

---

## Week 3–4 — Building an AI Chatbot

Topics

- Conversation State Management
- System Prompts
- Streaming Responses
- Basic Chat UI (CLI or simple web)

Exercises

- Build a multi-turn chatbot

Deliverable

Mini Project: AI Chatbot (v1)

---

## Week 5–6 — Embeddings & Vector Databases

Topics

- What Embeddings Are
- Similarity Search
- Vector Databases (e.g., Chroma or similar)
- Storing & Querying Embeddings

Exercises

- Build a semantic search tool over a small document set

Deliverable

Mini Project: Semantic Search Tool

---

## Week 7–8 — RAG (Retrieval-Augmented Generation)

Topics

- RAG Architecture
- Document Chunking Strategies
- Retrieval Pipeline
- Combining Retrieval With Generation

Exercises

- Build a RAG pipeline over Week 5–6 document set

Deliverable

Mini Project: RAG Assistant (v1)

---

## Week 9–10 — AI Agents & MCP

Topics

- What AI Agents Are
- Tool Use / Function Calling
- Intro to LangChain (or equivalent)
- Intro to MCP (Model Context Protocol)

Exercises

- Build a simple tool-using agent

Deliverable

Phase 5 Final Deliverable: AI Knowledge Base — RAG assistant with agent-style tool use

---

# Phase 6 — Production AI

Duration: Not yet finalized in ROADMAP.md (weekly breakdown to be added when this phase begins)

Topics (from ROADMAP.md)

- Docker
- Deployment
- Cloud
- Monitoring
- Scaling
- Security

Deliverable

Production AI Assistant

Note: A detailed weekly breakdown for this phase will be added closer to its start, once Phase 5 is complete, to keep planning realistic and up to date.

---

# Phase 7 — Career

Duration: Not yet finalized in ROADMAP.md (weekly breakdown to be added when this phase begins)

Topics (from ROADMAP.md)

- Resume
- LinkedIn
- GitHub
- Portfolio
- Interviews

Deliverables

- Professional Portfolio
- Interview Preparation
- AI Engineer Resume

---

# Final Capstone

Enterprise AI Platform

Combines all skills from Phases 1–6 into one production-ready application. Detailed scope will be defined once Phase 5 is complete.

---

# Notes on This Document

- Every phase's weekly plan follows the Teaching Method defined in MASTER_CONTEXT.md: Theory → Examples → Exercises → Mini Project → Review → Documentation → Git Commit.
- Every week must end with a Git commit per PROJECT_RULES.md (Rule 4).
- Math is intentionally excluded from the weekly topics per the student's profile — it will be introduced gradually only where a specific ML/LLM topic requires it.
- Phase 6 and 7 durations were not specified in ROADMAP.md, so their weekly breakdowns are intentionally left for later rather than invented now.

---

End of Version 1.0
