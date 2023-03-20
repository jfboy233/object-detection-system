import { createRouter, createWebHistory } from 'vue-router'


import Home from "@/views/Home";
import Login from "@/views/Login";
import Register from "@/views/Register";
import Layout from "@/Layout/Layout";
import Picture from "@/views/Picture";
import Blank from "@/views/blank"
import Video from "@/views/Video";
import Log from "@/views/Log";
import Instant from "@/views/Instant";
import Person from "@/views/Person";

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home,
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
    },
    {
        path: '/register',
        name: 'register',
        component: Register,
    },
    {
        path: '/system',
        name: 'Layout',
        component: Layout,
        redirect: "/system/picture",
        children: [
            {
                path: 'picture',
                name: 'Picture',
                component: Picture,
            },
            {
                path: 'video',
                name: 'Video',
                component: Video,
            },
            {
                path: 'instant',
                name: 'Instant',
                component: Instant,
            },
            {
                path: 'log',
                name: 'Log',
                component: Log,
            },
            {
                path: 'person',
                name: 'Person',
                component: Person,
            },
        ]
    },
    {
        path: '/blank',
        name: 'blank',
        component: Blank,
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router