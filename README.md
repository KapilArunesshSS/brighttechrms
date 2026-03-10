🏢 Brighttech RMS - Manpower Management & Recruitment System

Brighttech RMS is an industrial-grade human resource management platform and real-time attendance tracking system. It is engineered to handle high-density manpower data across multiple industrial sites including BMM, SLR, JAIRAJ, Arjas, MSSSL, and the consolidated AGNI complex.

Key Features

Intelligent Manpower Ledger (FFR) – Optimized for massive data grids with real-time performance analytics.

Dynamic Color-Coding – Integrated JavaScript logic highlights performance ratios $\ge 90\%$ in Emerald Green, while underperforming rows appear in Rose Red.

🛡️ Data Integrity Guard – Advanced backend logic in views.py that automatically identifies and clears redundant records during submission to prevent database conflicts.

🕹️ Moveable Dual-Axis Grid – Custom-engineered layout featuring vertical sticky headers and a horizontal sticky designation column for seamless navigation.

🔐 Multi-Site Authorization – Automated site-locking based on Username and Email credentials to ensure data isolation.

📈 Professional Reporting – Automated Excel exports with multi-row merged headers matching industrial compliance standards.

Technical Insights

Unified Site Logic – Streamlined handling for complex industrial clusters by consolidating multiple AGNI sub-units into a single common management interface.

Cloud Infrastructure – High-security document hosting using AWS S3 with Signed URLs for resumes and offer letters.

Memory Optimization – Configured to handle high-density form submissions (up to 2500 fields) to prevent server timeouts on low-memory environments.

Interactive Analytics – Live dashboard statistics providing granular visibility into hiring stages: Selected, Offered, Joined, Rejected, and Resigned.

Tech Stack

Backend: Python 3.12, Django Framework

Frontend: Tailwind CSS 3.x, Vanilla JavaScript, Lucide Icons

Database: PostgreSQL (Production), SQLite (Development)

Storage: AWS S3 (Signed Media Delivery)

Deployment: Vercel (CI/CD Pipeline)

Static Assets: WhiteNoise Middleware

Conclusion

The project demonstrates a production-ready solution for complex industrial manpower management. By combining robust Django security with a high-performance frontend grid, it provides a "Single Source of Truth" for attendance and recruitment across distributed geographical locations.

Developed for Bright Tech Industrials India Pvt Ltd.
