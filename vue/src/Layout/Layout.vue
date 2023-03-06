<template>
  <div>
    <Header/>
    <div>
      <Aside/>
      <router-view/>
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header";
import Aside from "@/components/Aside";
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Layout",
  components:{
    Header,
    Aside,
  },
}
</script>

<style scoped>

</style>