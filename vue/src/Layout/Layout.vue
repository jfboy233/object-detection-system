<template>
  <div style="width: 100%">
    <Header />
    <div style="display: flex">
      <Aside/>
      <router-view style="flex: 1"/>
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header";
import Aside from "@/components/Aside";
import request from "@/utils/request";
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Layout",
  components:{
    Header,
    Aside,
  },
  data(){
    return{
      user: {}
    }
  },
  methods:{

  },
  created() {
    // console.log(this.user)
    // this.refreshUser()
  }
}
</script>

<style scoped>

</style>