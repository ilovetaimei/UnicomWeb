<template>
  
</template>
<script>
export default {
  name: "App",
  data() {
    return {
      isActive: false,
      isActive1: false,
      isActive2: false,
      isSubShow: false
    };
  },
  methods: {
    sho() {
      if (this.isSubShow === true) {
        this.isSubShow = false;
      }
    },
    bt() {
      this.isSubShow = !this.isSubShow;
      this.isActive = true;
      this.isActive1 = false;
      this.isActive2 = false;
    },
    btn() {
      this.$router.push({ path: "/statement/polling" });
      this.isActive = true;
      if ((this.isActive = true)) {
        this.isActive1 = false;
        this.isActive2 = false;
      }
    },
    btn1() {
      this.$router.push({ path: "/statement/mesh" });
      this.isActive1 = true;
      if ((this.isActive1 = true)) {
        this.isActive = false;
        this.isActive2 = false;
      }
    },
    btn2() {
      this.$router.push({ path: "/statement/ping" });
      this.isActive2 = true;
      if ((this.isActive2 = true)) {
        this.isActive = false;
        this.isActive1 = false;
      }
    }
  },
  component: {
    app
  }
};
</script>
<style>
@import "../../assets/css/app.css";
</style>

