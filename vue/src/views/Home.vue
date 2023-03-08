<template>
  <div id="home" >
    <div :class="['bg', bg]" >
      <header >
        <nav >
          <ul>
            <li><a class="link-bio"  @click="bg = 'bio'">首页</a></li>
            <li><a class="link-projects"  @click="bg = 'projects'">关于我们</a></li>
            <li><a class="link-find-me"  @click="bg = 'find-me'">github</a></li>
          </ul>
        </nav>
        <div class="transition transition-bio"></div>
        <div class="transition transition-projects"></div>
        <div class="transition transition-find-me"></div>
        <h1>目标检测系统</h1>
      </header>
      <div class="dots dots1"></div>
      <div class="dots dots2"></div>
      <main>
        <transition name="slide-fade" mode="out-in">
            <p key="bio" v-if="bg==='bio'">
              <el-button type="danger" style="margin-top: 200px;" size="large" @click="start"><span>get start</span></el-button>
            </p>
            <p key="projects" v-else-if="bg==='projects'">This is a projects page.</p>
            <p key="find-me" v-else-if="bg==='find-me'">
              <el-button color="#E8E4D2" style="margin-top: 200px;" size="large" @click="github">
                <svg style="width: 20px;height: auto;" t="1678205780358" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2744" width="200" height="200"><path d="M1024 496C1012.8 232 798.4 17.6 534.4 8 393.6 1.6 259.2 52.8 156.8 150.4 56 248 0 379.2 0 520c0 230.4 155.2 433.6 376 492.8 6.4 1.6 12.8 3.2 19.2 3.2 16 0 32-4.8 44.8-16 17.6-14.4 28.8-35.2 28.8-57.6v-52.8c0-14.4 1.6-78.4 1.6-91.2 1.6-8 3.2-14.4 8-19.2 11.2-14.4 12.8-33.6 4.8-49.6-8-14.4-20.8-24-36.8-25.6-11.2-1.6-22.4-3.2-30.4-6.4-12.8-3.2-25.6-9.6-38.4-16-9.6-4.8-19.2-12.8-27.2-22.4-6.4-8-12.8-20.8-17.6-36.8-6.4-19.2-9.6-40-9.6-62.4 0-28.8 9.6-52.8 27.2-72l17.6-19.2-9.6-24c-3.2-8-6.4-19.2-4.8-38.4 22.4 8 28.8 12.8 28.8 12.8l1.6 1.6c6.4 3.2 11.2 8 16 9.6l19.2 11.2 16-4.8c27.2-8 54.4-11.2 83.2-11.2 28.8 0 56 3.2 83.2 11.2l16 4.8 33.6-20.8c11.2-6.4 22.4-12.8 35.2-17.6 1.6 14.4 0 27.2-4.8 40l-9.6 24 17.6 19.2c17.6 19.2 27.2 43.2 27.2 72 0 24-3.2 43.2-8 60.8-6.4 19.2-12.8 30.4-19.2 38.4-6.4 8-16 16-28.8 24-14.4 8-25.6 11.2-38.4 16-8 3.2-20.8 4.8-32 6.4h-1.6c-16 3.2-28.8 14.4-35.2 28.8-6.4 14.4-4.8 30.4 4.8 44.8 6.4 8 9.6 20.8 9.6 36.8v126.4c0 22.4 11.2 44.8 28.8 57.6 17.6 12.8 41.6 17.6 64 11.2C888 942.4 1035.2 729.6 1024 496zM651.2 931.2V816c0-14.4-1.6-27.2-4.8-38.4 17.6-4.8 35.2-11.2 54.4-22.4l1.6-1.6c20.8-12.8 36.8-25.6 49.6-41.6 16-19.2 25.6-41.6 33.6-64 8-25.6 12.8-52.8 12.8-86.4 0-41.6-11.2-76.8-33.6-108.8 6.4-33.6 3.2-67.2-11.2-104l-6.4-17.6-17.6-6.4c-17.6-6.4-40-4.8-67.2 6.4-17.6 6.4-33.6 14.4-51.2 24l-3.2 3.2c-56-12.8-116.8-12.8-174.4 0-1.6-1.6-3.2-1.6-4.8-3.2-9.6-6.4-24-14.4-46.4-22.4-27.2-12.8-51.2-14.4-70.4-8l-17.6 6.4-6.4 17.6c-14.4 38.4-17.6 72-9.6 104-22.4 30.4-33.6 67.2-33.6 108.8 0 30.4 3.2 57.6 12.8 84.8 8 27.2 19.2 49.6 32 65.6 16 17.6 32 32 51.2 41.6 17.6 9.6 35.2 17.6 54.4 22.4-1.6 4.8-1.6 9.6-3.2 16V843.2c-38.4-12.8-70.4-28.8-96-56-17.6-19.2-36.8-38.4-46.4-44.8-20.8-9.6-33.6 11.2-28.8 20.8 4.8 14.4 25.6 22.4 36.8 33.6 12.8 12.8 14.4 30.4 25.6 44.8 16 22.4 72 49.6 110.4 41.6v51.2C206.4 881.6 80 712 80 520c0-118.4 46.4-228.8 132.8-312C294.4 129.6 400 88 513.6 88h17.6C753.6 96 934.4 276.8 944 499.2c9.6 193.6-110.4 369.6-292.8 432z" p-id="2745" fill="#2c2c2c"></path></svg>
                <span style="margin-left: 15px">github</span>
              </el-button>
            </p>
        </transition>
      </main>
    </div>
  </div>
</template>

<script>
// import '../assets/jquery-3.1.1.min'
// import * as TweenMax from "core-js";
import '../assets/TweenMax.min'
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "home",
  data(){
    return {
      bg: 'bio',
      isDark: true,
    }
  },
  methods:{
    start() {
      this.$router.push('/login')
    },
    github() {
      window.location.href="https://github.com/jfboy233/object-detection-system/tree/main"
    }
  },
  mounted() {

  },
  watch: {

  },
}
</script>

<style lang="scss" >
:root {
  --purple-brown: #231f20;
  --egg-shell: #e8e4d2;
  --dark-peach: #e26961;
  --border-width: .75rem;
  --dots-gap: 10px;
}
*, *:before, *:after {
  box-sizing: border-box;
}
body {
  font-family: Trocchi, Georgia, serif;
  line-height: 1.5;
  color: var(--egg-shell);
}
a {
  color: inherit;
}

.bg {
  background: inherit;
  min-height: 100vh;
  padding: 25vh 0 1.5rem;
  transition: background 0s 1s, color .6s;
}
.projects {
  color: var(--purple-brown);
}

.bg:after {
   content: "";
   border: var(--border-width) solid;
   position: fixed;
   left: 0;
   top: 0;
   bottom: 0;
   right: 0;
   z-index: 12;
   pointer-events: none;
   transition: 1s;
  }

.bio,
.link-bio {
  background: var(--purple-brown);
}

.bio h1 {
  background-color: var(--dark-peach);
}
.projects,
.link-projects {
  background: var(--egg-shell);
}

.find-me,
.link-find-me {
  background: var(--dark-peach);
}


.transition {
   width: 1rem;
   height: 1rem;
   top: 0;
   display: block;
   position: absolute;
   opacity: 0;
   transition: transform .6s ease-in-out;
   width: 100%;
   height: 100vh;
   transform: scale(0.1);
   transform-origin: 0 0;
 }
.transition-bio {
  left: 0;
  background: var(--purple-brown);
}
.transition-projects {
  left: 7.5rem;
  background: var(--egg-shell);
}
.transition-find-me {
  left: 15rem;
  background: var(--dark-peach);
}

.bio .transition-bio,
.projects .transition-projects,
.find-me .transition-find-me {
  opacity: 1;
}
.bio .transition-bio {
  transform: scale(1);
}
.projects .transition-projects {
  transform: scale(1) translateX(-7.5rem) ;
}
.find-me .transition-find-me {
  transform: scale(1) translateX(-15rem) ;
}


.dots:before, .dots:after {
   content: "";
   position: fixed;
   top: 0;
   bottom: 0;
   opacity: .5;
   z-index: 11;
   background-image: linear-gradient(var(--dark-peach) 20%,transparent 0);
   background-size: 100% var(--dots-gap);
   background-position: 0 0;
   animation: movebg .2s linear infinite;
   will-change: transform;
   width: 2px;
  }

.dots1:before {
  left: 5%;
}
.dots1:after {
  left: 15%;
}
.dots2:before {
  right: 75%;
}
.dots2:after {
  right: 5%;
}

.dots:after {
  animation-direction: reverse;
}

.find-me {
  .dots:before,
  .dots:after {
    background-image: linear-gradient(var(--egg-shell) 20%,transparent 0);
  }
}

@keyframes movebg {
  0% {
    transform: translate3d(0, 0, 0);
  }
  100% {
    transform: translate3d(0, var(--dots-gap), 0);
  }
}



 h1 {
   font-family: "Anton", sans-serif;
   text-align: center;
   margin: 0;
   -webkit-background-clip: text;
   -webkit-text-fill-color: transparent;
   -webkit-mask-image: -webkit-gradient(linear,left top,left bottom,color-stop(0,#000),color-stop(.5,#000),color-stop(1,transparent));
   transition: background-position 1s, background-color 1s;
   text-align: center;
   font-size: calc(14vw + 1rem);
   font-weight: 200;
   line-height: 1;
   background-image: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/74321/tw-o.png'), url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/74321/tw6-o.png'), url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/74321/tw5-o.png');
   background-size: 45vw auto, 45vw auto, 30vw auto;
   background-repeat: repeat-x;
   background-position: 0px 15%, 200px 25%, -50px 2vw;
 }
.projects h1 {
  background-color: var(--dark-peach);
  background-position: -120px 15%, 230px 20%, -100px 3vw;
}
.find-me h1 {
  background-color: var(--egg-shell);
  background-position: -240px 15%, 260px 25%, -150px 1vw;
}


nav {
  position: fixed;
  top: var(--border-width);
  left: var(--border-width);
  z-index: 10;
  ul {
  list-style: none;
  display: flex;
  text-align: center;
  margin: 0;
  padding: 0;
  }
  li {
  flex: 1 0 7.5rem;
  }
  a {
  display: block;
  padding: .75rem 0 .5rem;
  color: var(--egg-shell);
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-size: .875rem;
  }
  .link-projects {
  color: var(--purple-brown);
  }
}


 main {
   position: relative;
   max-width: 36rem;
   padding: 0 1.5rem;
   margin: -3rem auto 0;
   font-size: 2rem;
 }


.slide-fade-enter-active {
     transition: all 1s ease;
   }
.slide-fade-leave-active {
  transition: all .5s;
}
.slide-fade-enter, .slide-fade-leave-to {
  transform: translateY(2rem);
  opacity: 0;
}
</style>