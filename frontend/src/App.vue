<template>
  <div id="app">
    <AppSidebar :onSidebarStateChange="updateSidebarState" />
    <div :class="['main-content', { collapsed: isCollapsed }]">
      <router-view />
    </div>
  </div>
</template>

<script>
import AppSidebar from './components/Sidebar.vue'

export default {
  components: { AppSidebar },
  data() {
    return {
      isCollapsed: false,
    }
  },
  methods: {
    updateSidebarState(collapsed) {
      this.isCollapsed = collapsed;
    }
  }
};
</script>

<style>
body.light {
  background-color: #ffffff;
  color: #000000;
}

body.dark {
  background-color: #1e1e1e;
  color: #000000;
}

.sidebar {
  transition: background-color 0.3s;
}
body.light .sidebar {
  background-color: #f0f0f0;
}
body.dark .sidebar {
  background-color: #2e2e2e;
}

#app  {
  display: flex;
}

#main-content {
  margin-left: 250px;
  padding: 20px;
  width: 100%;
  transition: margin-left 0.3s ease;
}

#sidebar-container.collapsed + #main-content {
  margin-left: 60px;
}
</style>
