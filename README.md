<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brighttech RMS | Industrial Manpower Solution</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Great+Vibes&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; scroll-behavior: smooth; }
        .elegant-script { font-family: 'Great Vibes', cursive; }
        .glass-effect { background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(12px); }
        .feature-card:hover { transform: translateY(-5px); transition: all 0.3s ease; }
        .gradient-text { background: linear-gradient(135deg, #1e293b 0%, #2563eb 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    </style>
</head>
<body class="bg-slate-50 text-slate-900 overflow-x-hidden">

    <!-- Navigation -->
    <nav class="fixed w-full z-50 glass-effect border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center text-white shadow-lg shadow-blue-200">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
                </div>
                <span class="text-xl font-extrabold tracking-tighter text-slate-900 uppercase">Brighttech <span class="text-blue-600">RMS</span></span>
            </div>
            <div class="hidden md:flex items-center gap-8 text-sm font-bold uppercase tracking-widest text-slate-500">
                <a href="#ledger" class="hover:text-blue-600 transition">FFR Ledger</a>
                <a href="#security" class="hover:text-blue-600 transition">Auth</a>
                <a href="#database" class="hover:text-blue-600 transition">Database</a>
                <a href="#tech" class="hover:text-blue-600 transition">Stack</a>
            </div>
            <a href="https://github.com/KapilArunesshSS/brighttechrms" class="bg-slate-900 text-white px-6 py-3 rounded-full text-sm font-bold hover:bg-black transition shadow-xl shadow-slate-200">
                GitHub Repo
            </a>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative pt-40 pb-20 px-6 overflow-hidden">
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-[600px] bg-gradient-to-b from-blue-50 to-transparent -z-10"></div>
        <div class="max-w-5xl mx-auto text-center">
            <div class="inline-flex items-center gap-2 bg-white px-4 py-2 rounded-full border border-blue-100 shadow-sm mb-8 animate-bounce">
                <span class="w-2 h-2 bg-blue-500 rounded-full"></span>
                <span class="text-[10px] font-black uppercase tracking-widest text-blue-600">Enterprise v2.0 Live</span>
            </div>
            <h1 class="text-5xl md:text-7xl font-extrabold tracking-tighter text-slate-900 mb-6 leading-[1.1]">
                Manpower Management <br> <span class="gradient-text">Redefined for Industry.</span>
            </h1>
            <p class="text-lg text-slate-500 max-w-2xl mx-auto mb-10 leading-relaxed font-medium">
                A specialized HR platform designed to streamline recruitment workflows and daily attendance tracking across major industrial sites including BMM, SLR, and AGNI.
            </p>
            <div class="elegant-script text-4xl text-blue-600 mb-12">"Rise Above The Rest"</div>
            <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                <button class="w-full sm:w-auto px-8 py-4 bg-blue-600 text-white font-bold rounded-2xl shadow-2xl shadow-blue-300 hover:bg-blue-700 transition transform active:scale-95">Explore Features</button>
                <button class="w-full sm:w-auto px-8 py-4 bg-white text-slate-700 border border-slate-200 font-bold rounded-2xl hover:bg-slate-50 transition shadow-sm">View Documentation</button>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section id="ledger" class="py-24 px-6 bg-white">
        <div class="max-w-7xl mx-auto">
            <div class="mb-20 text-center">
                <h2 class="text-3xl font-black tracking-tight text-slate-900 mb-4">Core Ecosystem Features</h2>
                <div class="w-20 h-1.5 bg-blue-600 mx-auto rounded-full"></div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <!-- Ledger Card -->
                <div class="feature-card p-8 rounded-[2rem] bg-slate-50 border border-slate-100">
                    <div class="w-14 h-14 bg-emerald-100 text-emerald-600 rounded-2xl flex items-center justify-center mb-6 shadow-sm">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"></line><line x1="18" y1="20" x2="18" y2="4"></line><line x1="6" y1="20" x2="6" y2="16"></line></svg>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-4 tracking-tight">Intelligent Ledger</h3>
                    <p class="text-slate-500 text-sm leading-relaxed mb-4">Dynamic FFR & Absenteeism calculations with real-time emerald/rose color coding for instant site performance feedback.</p>
                    <ul class="text-[11px] font-bold text-slate-400 space-y-2 uppercase tracking-wide">
                        <li>• Duplicate Protection</li>
                        <li>• Dual-Axis Navigation</li>
                    </ul>
                </div>

                <!-- Security Card -->
                <div id="security" class="feature-card p-8 rounded-[2rem] bg-slate-50 border border-slate-100">
                    <div class="w-14 h-14 bg-indigo-100 text-indigo-600 rounded-2xl flex items-center justify-center mb-6 shadow-sm">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-4 tracking-tight">Multi-Site Auth</h3>
                    <p class="text-slate-500 text-sm leading-relaxed mb-4">Enterprise security mapping based on both Email and Username. Site locking ensures data isolation per site administrator.</p>
                    <ul class="text-[11px] font-bold text-slate-400 space-y-2 uppercase tracking-wide">
                        <li>• Site Locking Logic</li>
                        <li>• Superuser Control</li>
                    </ul>
                </div>

                <!-- Database Card -->
                <div id="database" class="feature-card p-8 rounded-[2rem] bg-slate-50 border border-slate-100">
                    <div class="w-14 h-14 bg-amber-100 text-amber-600 rounded-2xl flex items-center justify-center mb-6 shadow-sm">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></ellipse></svg>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-4 tracking-tight">Recruitment DB</h3>
                    <p class="text-slate-500 text-sm leading-relaxed mb-4">Centralized applicant tracking with unique ID generation and AWS S3 integration for resumes and offer letters.</p>
                    <ul class="text-[11px] font-bold text-slate-400 space-y-2 uppercase tracking-wide">
                        <li>• Pipeline Analytics</li>
                        <li>• AWS S3 Storage</li>
                    </ul>
                </div>

                <!-- Reporting Card -->
                <div class="feature-card p-8 rounded-[2rem] bg-slate-50 border border-slate-100">
                    <div class="w-14 h-14 bg-blue-100 text-blue-600 rounded-2xl flex items-center justify-center mb-6 shadow-sm">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-4 tracking-tight">Reporting Engine</h3>
                    <p class="text-slate-500 text-sm leading-relaxed mb-4">Automated Excel exports with multi-row merged headers and horizontal pivot monthly summaries using Openpyxl.</p>
                    <ul class="text-[11px] font-bold text-slate-400 space-y-2 uppercase tracking-wide">
                        <li>• Pivot summaries</li>
                        <li>• Merged Cell logic</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Tech Stack Section -->
    <section id="tech" class="py-24 px-6 bg-slate-50">
        <div class="max-w-4xl mx-auto">
            <div class="bg-slate-900 rounded-[3rem] p-10 md:p-16 text-white shadow-3xl">
                <h2 class="text-3xl font-black mb-12 tracking-tight text-center">Technical Architecture</h2>
                
                <div class="grid grid-cols-2 md:grid-cols-3 gap-y-12 gap-x-8">
                    <div class="text-center">
                        <div class="text-blue-400 text-[10px] font-black uppercase tracking-widest mb-2">Backend</div>
                        <div class="text-xl font-bold">Python / Django</div>
                    </div>
                    <div class="text-center">
                        <div class="text-blue-400 text-[10px] font-black uppercase tracking-widest mb-2">Frontend</div>
                        <div class="text-xl font-bold">Tailwind CSS</div>
                    </div>
                    <div class="text-center">
                        <div class="text-blue-400 text-[10px] font-black uppercase tracking-widest mb-2">Database</div>
                        <div class="text-xl font-bold">PostgreSQL</div>
                    </div>
                    <div class="text-center">
                        <div class="text-blue-400 text-[10px] font-black uppercase tracking-widest mb-2">Object Storage</div>
                        <div class="text-xl font-bold">AWS S3</div>
                    </div>
                    <div class="text-center">
                        <div class="text-blue-400 text-[10px] font-black uppercase tracking-widest mb-2">Deployment</div>
                        <div class="text-xl font-bold">Vercel</div>
                    </div>
                    <div class="text-center">
                        <div class="text-blue-400 text-[10px] font-black uppercase tracking-widest mb-2">Excel Engine</div>
                        <div class="text-xl font-bold">Openpyxl</div>
                    </div>
                </div>

                <div class="mt-20 pt-10 border-t border-slate-800">
                    <h4 class="text-sm font-black uppercase tracking-widest text-slate-500 mb-6 text-center">Production Infrastructure</h4>
                    <p class="text-slate-400 text-center text-sm leading-relaxed max-w-2xl mx-auto">
                        Optimized for Vercel using custom build scripts. Static assets handled via WhiteNoise. Media security managed via Boto3 with private signed S3 URL generation.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="py-12 border-t border-slate-200">
        <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
            <div class="text-slate-400 text-xs font-bold uppercase tracking-widest">
                © 2024 Bright Tech Industrials India Pvt Ltd. All rights reserved.
            </div>
            <div class="flex items-center gap-6 text-slate-400">
                <a href="#" class="hover:text-blue-600 transition font-bold text-xs uppercase tracking-widest">Privacy</a>
                <a href="#" class="hover:text-blue-600 transition font-bold text-xs uppercase tracking-widest">Terms</a>
                <a href="#" class="hover:text-blue-600 transition font-bold text-xs uppercase tracking-widest">Support</a>
            </div>
        </div>
    </footer>

</body>
</html>
