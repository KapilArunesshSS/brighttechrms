<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DMRM Project Documentation</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
        body { font-family: 'Inter', sans-serif; }
        code, pre { font-family: 'JetBrains Mono', monospace; }
        .section-border { border-bottom: 1px solid #e2e8f0; padding-bottom: 2rem; margin-bottom: 2rem; }
    </style>
</head>
<body class="bg-white text-slate-800 antialiased">

    <div class="max-w-3xl mx-auto px-6 py-16">
        <!-- Header -->
        <header class="mb-12 border-b-2 border-slate-900 pb-8">
            <h1 class="text-4xl font-bold tracking-tight text-slate-900 mb-2">DMRM System</h1>
            <p class="text-lg text-slate-500 font-medium">Recruitment Management & Filling Factor Ratio (FFR) Ledger</p>
            <div class="mt-4 flex gap-4 text-xs font-bold uppercase tracking-widest text-slate-400">
                <span>Production v1.0</span>
                <span class="text-slate-200">|</span>
                <span>AWS Hybrid Architecture</span>
            </div>
        </header>

        <!-- Overview -->
        <section class="section-border">
            <h2 class="text-sm font-bold uppercase tracking-widest text-indigo-600 mb-4">Project Overview</h2>
            <p class="leading-relaxed text-slate-600">
                DMRM is a professional-grade HR and operations ecosystem designed for industrial manpower tracking. The system specializes in real-time **Filling Factor Ratio (FFR)** calculations, transforming manual manpower logs into actionable digital data for site supervisors and management.
            </p>
        </section>

        <!-- Features -->
        <section class="section-border">
            <h2 class="text-sm font-bold uppercase tracking-widest text-indigo-600 mb-4">Operational Features</h2>
            <div class="grid grid-cols-1 gap-4">
                <div class="flex gap-4">
                    <span class="font-bold text-slate-300">01</span>
                    <div>
                        <h3 class="font-semibold text-slate-900">FFR Analytics</h3>
                        <p class="text-sm text-slate-500">Automated calculation of manpower efficiency across multiple industrial sites.</p>
                    </div>
                </div>
                <div class="flex gap-4">
                    <span class="font-bold text-slate-300">02</span>
                    <div>
                        <h3 class="font-semibold text-slate-900">Workforce Lifecycle</h3>
                        <p class="text-sm text-slate-500">Comprehensive CRUD operations for recruitment, onboarding, and profile management.</p>
                    </div>
                </div>
                <div class="flex gap-4">
                    <span class="font-bold text-slate-300">03</span>
                    <div>
                        <h3 class="font-semibold text-slate-900">Secure Access</h3>
                        <p class="text-sm text-slate-500">Role-based authentication ensuring sensitive HR data isolation.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Technical Structure -->
        <section class="section-border">
            <h2 class="text-sm font-bold uppercase tracking-widest text-indigo-600 mb-4">Directory Structure</h2>
            <div class="bg-slate-50 border border-slate-200 rounded-lg p-5">
                <pre class="text-xs text-slate-700 leading-6">
DMRM/
├── main/                   <span class="text-slate-400"># Primary App logic</span>
│   ├── templates/          <span class="text-slate-400"># dashboard.html, ffr.html, auth/</span>
│   ├── models.py           <span class="text-slate-400"># Workforce & FFR schemas</span>
│   └── views.py            <span class="text-slate-400"># Business logic & calculations</span>
├── server/                 <span class="text-slate-400"># WSGI configuration for cPanel</span>
├── staticfiles/            <span class="text-slate-400"># Production assets</span>
├── .env                    <span class="text-slate-400"># AWS/Database credentials</span>
└── requirements.txt        <span class="text-slate-400"># System dependencies</span></pre>
            </div>
        </section>

        <!-- Infrastructure -->
        <section class="section-border">
            <h2 class="text-sm font-bold uppercase tracking-widest text-indigo-600 mb-4">Cloud Infrastructure</h2>
            <table class="w-full text-sm text-left">
                <thead class="text-xs text-slate-400 uppercase">
                    <tr>
                        <th class="pb-3 pr-4">Service</th>
                        <th class="pb-3">Utility</th>
                    </tr>
                </thead>
                <tbody class="text-slate-600 divide-y divide-slate-100">
                    <tr>
                        <td class="py-3 pr-4 font-semibold text-slate-900">AWS EC2</td>
                        <td class="py-3">Application hosting and compute logic.</td>
                    </tr>
                    <tr>
                        <td class="py-3 pr-4 font-semibold text-slate-900">AWS RDS</td>
                        <td class="py-3">Managed database for persistent HR records.</td>
                    </tr>
                    <tr>
                        <td class="py-3 pr-4 font-semibold text-slate-900">AWS S3</td>
                        <td class="py-3">Object storage for media and static delivery.</td>
                    </tr>
                </tbody>
            </table>
        </section>

        <!-- Deployment -->
        <section class="mb-16">
            <h2 class="text-sm font-bold uppercase tracking-widest text-indigo-600 mb-4">Deployment Workflow</h2>
            <div class="space-y-4">
                <div class="p-4 border border-slate-200 rounded-lg">
                    <h4 class="text-sm font-bold text-slate-900 mb-1">Production (cPanel)</h4>
                    <p class="text-xs text-slate-500">The professional backend environment managed via Python Setup App and WSGI integration.</p>
                </div>
                <div class="p-4 border border-slate-200 rounded-lg bg-slate-50">
                    <h4 class="text-sm font-bold text-slate-900 mb-1">Reference (Vercel)</h4>
                    <p class="text-xs text-slate-500">Edge deployment for frontend performance benchmarking and UI reference.</p>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="flex justify-between items-center text-[10px] font-bold uppercase tracking-widest text-slate-300">
            <span>DMRM Technical Documentation</span>
            <span>&copy; 2026</span>
        </footer>
    </div>

</body>
</html>
