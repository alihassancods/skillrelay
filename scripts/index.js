// Function to disable scrolling
const disableScroll = () => {
    document.body.classList.add('no-scroll');
};

// Additional check if page is refreshed in the middle
window.addEventListener('beforeunload', () => {
    // Re-enable scroll if the page is being unloaded (user navigates or refreshes)
    enableScroll();
});
// Function to enable scrolling
const enableScroll = () => {
    document.body.classList.remove('no-scroll');
};
disableScroll();

tl = gsap.timeline()
tl.from('.page1 > *',{
    duration: 0.5,
  y: '100%',
  delay:1,
  opacity: 0,
  stagger: 0.1,
  ease: 'power2.out',
})
tl.to('.page1',{
    height : "0vh",
    backgroundColor: "black",
    duration : 1,
    delay : 0.5,
})
tl.from('nav a',{
    y: "100%",
    duration : 0.5,
    delay : 0.5,
    stagger : 0.1,
    ease: "power2.out",
    opacity : 0,
})
tl.from('#hero-section h1',{
    x:"-10%",
    y:"50%",
    stagger : 0.1,
    duration:0.5,
    delay:0.5,
    opacity:0,
})
tl.from('#laptop',{
    x:"10%",
    y:"-10%",
    delay:0.5,
    duration:1,
    opacity:0,
    onComplete: () => {
        enableScroll();
    }
})
const path = document.getElementById("path")
const fCircle1 = document.getElementById("feature-circle-1")
const fCircle2 = document.getElementById("feature-circle-2")
const fCircle3 = document.getElementById("feature-circle-3")
path.addEventListener("mouseenter",()=>{
    gsap.to(path,{
        height : 450,
        duration : 5
    })
})