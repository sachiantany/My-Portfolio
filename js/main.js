/* ── Scroll & nav ── */
window.addEventListener('scroll', () => {
    const pct = window.scrollY / (document.body.scrollHeight - window.innerHeight) * 100;
    document.getElementById('sp').style.width = pct + '%';
    document.getElementById('nav').classList.toggle('scrolled', window.scrollY > 40);
});

/* ── Mobile menu ── */
function openMob() {
    document.getElementById('mobMenu').classList.add('open');
    document.body.style.overflow = 'hidden';
}
function closeMob() {
    document.getElementById('mobMenu').classList.remove('open');
    document.body.style.overflow = '';
}
document.addEventListener('keydown', e => { if (e.key === 'Escape') { closeMob(); closeAllModals(); } });

/* ── Fade-up observer ── */
const fuObs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('vis'); });
}, { threshold: 0.08 });
document.querySelectorAll('.fu').forEach(el => fuObs.observe(el));

/* ── Unified modal system ── */
const modalMap = {
    ht:    { id: 'htImageSliderModal',      total: 9, counter: 'currentHtSlide' },
    rc:    { id: 'imageSliderModal',        total: 7, counter: 'currentSlide' },
    dl:    { id: 'dilmahImageSliderModal',  total: 5, counter: 'currentDilmahSlide' },
    san:   { id: 'sanasaImageSliderModal',  total: 3, counter: 'currentSanasaSlide' },
    doc:   { id: 'docItImageSliderModal',   total: 2, counter: 'currentDocItSlide' },
    bns:   { id: 'bnsImageSliderModal',     total: 2, counter: 'currentBnsSlide' },
    lh:    { id: 'lhImageSliderModal',      total: 2, counter: 'currentLhSlide' },
};
const sliderIdx = {};

function showSlideFor(key, n) {
    const cfg = modalMap[key];
    if (!cfg) return;
    const modal = document.getElementById(cfg.id);
    const slides = modal.querySelectorAll('.slider-image');
    const dots   = modal.querySelectorAll('.slider-dot');
    let idx = n;
    if (idx > cfg.total) idx = 1;
    if (idx < 1) idx = cfg.total;
    sliderIdx[key] = idx;
    slides.forEach(s => s.classList.remove('active'));
    dots.forEach(d => d.classList.remove('active'));
    if (slides[idx-1]) slides[idx-1].classList.add('active');
    if (dots[idx-1])   dots[idx-1].classList.add('active');
    const ctr = document.getElementById(cfg.counter);
    if (ctr) ctr.textContent = idx;
}
function nextSlide(key)  { showSlideFor(key, (sliderIdx[key]||1) + 1); }
function prevSlide(key)  { showSlideFor(key, (sliderIdx[key]||1) - 1); }
function goSlide(key, n) { showSlideFor(key, n); }

function openModal(id, key) {
    document.getElementById(id).style.display = 'flex';
    document.body.style.overflow = 'hidden';
    if (key) showSlideFor(key, 1);
}
function closeModal(id) {
    document.getElementById(id).style.display = 'none';
    document.body.style.overflow = '';
}
function closeAllModals() {
    document.querySelectorAll('.image-slider-modal').forEach(m => { m.style.display = 'none'; });
    document.body.style.overflow = '';
}

/* Named openers kept for onclick compatibility */
function openImageSlider()       { openModal('imageSliderModal', 'rc'); }
function closeImageSlider()      { closeModal('imageSliderModal'); }
function openDilmahImageSlider() { openModal('dilmahImageSliderModal', 'dl'); }
function closeDilmahImageSlider(){ closeModal('dilmahImageSliderModal'); }
function openSanasaImageSlider() { openModal('sanasaImageSliderModal', 'san'); }
function closeSanasaImageSlider(){ closeModal('sanasaImageSliderModal'); }
function openLitroImageSlider()  { openModal('litroImageSliderModal', null); }
function closeLitroImageSlider() { closeModal('litroImageSliderModal'); }
function openDocItImageSlider()  { openModal('docItImageSliderModal', 'doc'); }
function closeDocItImageSlider() { closeModal('docItImageSliderModal'); }
function openHtImageSlider()     { openModal('htImageSliderModal', 'ht'); }
function closeHtImageSlider()    { closeModal('htImageSliderModal'); }
function openBnsImageSlider()    { openModal('bnsImageSliderModal', 'bns'); }
function closeBnsImageSlider()   { closeModal('bnsImageSliderModal'); }
function openLhImageSlider()     { openModal('lhImageSliderModal', 'lh'); }
function closeLhImageSlider()    { closeModal('lhImageSliderModal'); }

/* Backdrop click closes modal */
document.querySelectorAll('.image-slider-modal').forEach(m => {
    m.addEventListener('click', e => { if (e.target === m) closeAllModals(); });
});

/* Keyboard arrow navigation for open modal */
document.addEventListener('keydown', e => {
    const open = Array.from(document.querySelectorAll('.image-slider-modal'))
                      .find(m => m.style.display === 'flex');
    if (!open) return;
    const key = Object.keys(modalMap).find(k => modalMap[k].id === open.id);
    if (!key) return;
    if (e.key === 'ArrowRight') nextSlide(key);
    if (e.key === 'ArrowLeft')  prevSlide(key);
});

/* ── Contact form ── */
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const name    = document.getElementById('name').value;
    const email   = document.getElementById('email').value;
    const subject = document.getElementById('subject').value;
    const message = document.getElementById('message').value;
    const body    = `Name: ${name}%0D%0AEmail: ${email}%0D%0A%0D%0A${message}`;
    window.location.href = `mailto:sachi.antany@gmail.com?subject=${encodeURIComponent(subject)}&body=${body}`;
});
