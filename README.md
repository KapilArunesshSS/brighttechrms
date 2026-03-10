Brighttech RMS - Manpower Management & Recruitment System

Brighttech RMS is a specialized industrial human resource management platform designed to streamline recruitment workflows and daily manpower attendance tracking across multiple industrial sites (BMM, SLR, JAIRAJ, Arjas, MSSSL, and AGNI).

🚀 Key Features

1. Intelligent Manpower Ledger (FFR)

The core of the system is the Filling Factor Ratio (FFR) ledger, which allows site administrators to manage daily attendance, weekly offs, and overtime.

Duplicate Protection: Backend logic automatically detects and clears redundant records for specific dates/designations to ensure data integrity.

Dynamic UI: Live JavaScript calculations for FFR and Absenteeism percentages.

Smart Color-Coding: Real-time visual feedback where FFR $\ge 90\%$ is highlighted in emerald green and below $90\%$ in rose red.

Dual-Axis Navigation: A flexible, "moveable" grid layout with sticky headers and sticky designation columns for easy data entry in large datasets.

2. Multi-Site Authorization

Strict security mapping based on both Username and Email ensures that site-level administrators only see and edit data for their assigned locations.

Superuser Control: Global view access for administrators to monitor all sites simultaneously.

Unified Site Logic: Consolidated handling for complex sites like AGNI, treating multiple units as a single management entity.

3. Comprehensive Recruitment Database

Candidate Management: Automated unique Reference ID generation (e.g., RMS0001).

Cloud Storage: Integrated with AWS S3 for secure, scalable hosting of candidate resumes and official offer letters.

Pipeline Analytics: Dashboard stats providing a bird's-eye view of Selected, Offered, Joined, and Rejected candidates.

4. Professional Reporting Engine

Advanced Excel export functionality using openpyxl:

Daily Reports: Multi-row merged headers formatted to industrial standards.

Monthly Summaries: Horizontal pivot-style reports aggregating performance across custom date ranges.

🛠 Tech Stack

Backend: Python / Django

Frontend: Tailwind CSS, Vanilla JavaScript, Lucide Icons

Database: PostgreSQL (Production) / SQLite (Development)

Cloud Infrastructure: AWS S3 (Media), Vercel (Hosting)

Reporting: Openpyxl

📦 Deployment Configuration

The project is optimized for deployment on Vercel with custom build scripts (build_files.sh) and specialized Django settings to handle static files via WhiteNoise and media files via Boto3. This ensures high availability and secure handling of sensitive HR documents.

Developed for Bright Tech Industrials India Pvt Ltd.
