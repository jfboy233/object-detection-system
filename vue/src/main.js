import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElIconModules from '@element-plus/icons'

import axios from "axios"



const app = createApp(App)
for(let iconName in ElIconModules){
    app.component(iconName,ElIconModules[iconName])
}
axios.defaults.withCredentials = true
app.use(router).use(ElementPlus).mount('#app')