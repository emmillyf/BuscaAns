<template>
  <div id="sidebar-container" 
       :class="[
       { collapsed: isCollapsed, mobile: isMobile },
       isDarkMode ? 'dark' : '' ]"
       @mouseenter="hoverSidebar"
       @mouseleave="leaveSidebar">
    <div class="sidebar-overlay" v-if="isMobile && !isCollapsed" @click="toggleSidebar"></div>
    
    <div id="sidebar">
      <div class="sidebar-header"  v-if="isMobile && !isCollapsed">
        <i class='bx bx-menu mobile-menu-icon' @click="toggleSidebar" ></i>
      </div>
      
      <div id="menu" v-show="!isCollapsed || isHovered">
        <div class="menu-section">
          <router-link to="/operadoras/buscar/" class="menu-item" exact-active-class="active-link">
            <i class='bx bx-home-alt-2'></i> <span class="menu-text">Início</span></router-link>
        </div>
        
        <div class="menu-section">
          <router-link to="/operadoras" class="menu-item" exact-active-class="active-link">
            <i class='bx bxs-file'></i> <span class="menu-text">Lista de Operadoras</span></router-link>
        </div>
        
        <div class="menu-section">
          <h3 @click="downloadCSV"> 
          <i class='bx bx-export'></i> <span class="menu-text">Exportar CSV</span></h3>
        </div>

        <div class="theme-toggle" @click="toggleTheme">
          <i  :class="isDark ? 'bx bx-sun' : 'bx bx-moon'"></i>
          <span class="menu-text">{{ isDark ? 'Light Mode' : 'Dark Mode' }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'AppSidebar',
  data() {
    return {
      isCollapsed: false,
      isMobile: false,
      isHovered: false,
      mobileBreakpoint: 768,
      isDarkMode: false
    }
  },
  mounted (){
    const storedTheme = localStorage.getItem('theme')
    this.isDarkMode = storedTheme === 'dark'
    document.body.className = this.isDarkMode ? 'dark' : 'light'

    this.isCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
    this.checkScreenSize();
    window.addEventListener('resize', this.checkScreenSize);
  },
  methods: {
    navigateTo(route) {
    this.$router.push(route);
    if (this.isMobile) this.toggleSidebar();
  },
  toggleTheme() {
      this.isDarkMode = !this.isDarkMode;
      document.body.className = this.isDarkMode ? 'dark' : 'light';
      localStorage.setItem('theme', this.isDarkMode ? 'dark' : 'light');
    },
    toggleSidebar() {
      this.isCollapsed = !this.isCollapsed;
      localStorage.setItem('sidebarCollapsed', this.isCollapsed);
    },
    checkScreenSize() {
      const isNowMobile = window.innerWidth < this.mobileBreakpoint;
      if (isNowMobile !== this.isMobile) {
      this.isMobile = isNowMobile;
      this.isCollapsed = true; 
  }
    },
    hoverSidebar() {
      if (!this.isMobile && this.isCollapsed) {
        this.isHovered = true;
      }
    },
    leaveSidebar() {
      this.isHovered = false;
    },
      async downloadCSV() {
        fetch('http://localhost:8000/download-csv')
        .then(res => res.blob())
        .then(blob => {
        const url = URL.createObjectURL(blob)
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', 'Relatorio_cadop.csv')
        document.body.appendChild(link)
        link.click()
        link.remove()
      })
    }
  }
};
</script>

<style scoped>
* {
  font-family: "Poppins", sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  transition: all 0.3s ease;
}

#sidebar-container {
  width: 250px;
  height: 100vh;
  background: #FFFFFF;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  position: fixed;
  left: 0;
  top: 0;
  z-index: 1000;
  overflow: hidden;
}

#sidebar-container.dark {
  background: #2a2a2a;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
}

#sidebar-container.collapsed {
  width: 60px;
}

#sidebar-container.mobile {
  width: 60px;
  box-shadow: none;
}

#sidebar-container.mobile.collapsed {
  width: 60px;
}

#sidebar-container.mobile:not(.collapsed) {
  width: 250px;
  z-index: 1001;
  box-shadow: 5px 0 15px rgba(0, 0, 0, 0.2);
}

.sidebar-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

#sidebar {
  padding: 20px 15px;
  display: flex;
  flex-direction: column;
  height: 100%;
  background: inherit;
  position: relative;
  z-index: 1001;
}

.sidebar-header {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 30px;
}

.mobile-menu-icon {
  font-size: 24px;
  color: #980020;
  cursor: pointer;
  padding: 5px;
  border-radius: 50%;
}

.mobile-menu-icon:hover {
  background-color: rgba(152, 0, 32, 0.1);
}

#sidebar-container.dark .mobile-menu-icon {
  color: #ff6b6b;
}

#sidebar-container.dark .mobile-menu-icon:hover {
  background-color: rgba(255, 107, 107, 0.1);
}

.chevron-icon {
  font-size: 24px;
  color: #980020;
  cursor: pointer;
  padding: 5px;
  border-radius: 50%;
}

.chevron-icon:hover {
  background-color: rgba(152, 0, 32, 0.1);
}

#sidebar-container.dark .chevron-icon {
  color: #ff6b6b;
}

#sidebar-container.dark .chevron-icon:hover {
  background-color: rgba(255, 107, 107, 0.1);
}

#menu {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px;
  border-radius: 6px;
  white-space: nowrap;
  font-size: 0.9rem;
  font-weight: 500;
  color: #555555;
  text-decoration: none; /* Remove underline */
}

.menu-item:hover {
  background-color: rgba(152, 0, 32, 0.1);
  color: #980020;
}

#sidebar-container.dark .menu-item {
  color: #dddddd;
}

#sidebar-container.dark .menu-item:hover {
  background-color: rgba(255, 107, 107, 0.1);
  color: #ff6b6b;
}

.active-link {
  font-weight: bold;
  color: #980020;
}

#sidebar-container.dark .active-link {
  color: #ff6b6b;
}

.menu-section {
  margin-bottom: 20px;
}

.menu-section h2, .menu-section h3 {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px;
  margin: 0;
  cursor: pointer;
  border-radius: 6px;
  white-space: nowrap;
}

.menu-section h2 {
  font-size: 1rem;
  font-weight: 600;
  color: #333333;
}

.menu-section h3 {
  font-size: 0.9rem;
  font-weight: 500;
  color: #555555;
}

#sidebar-container.dark .menu-section h2 {
  color: #ffffff;
}

#sidebar-container.dark .menu-section h3 {
  color: #dddddd;
}

.menu-section h2:hover, .menu-section h3:hover {
  background-color: rgba(152, 0, 32, 0.1);
  color: #980020;
}

#sidebar-container.dark .menu-section h2:hover,
#sidebar-container.dark .menu-section h3:hover {
  background-color: rgba(255, 107, 107, 0.1);
  color: #ff6b6b;
}

.theme-toggle {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px;
  margin-top: auto;
  cursor: pointer;
  color: #555555;
  border-radius: 6px;
}

#sidebar-container.dark .theme-toggle {
  color: #dddddd;
}

.theme-toggle:hover {
  background-color: rgba(152, 0, 32, 0.1);
  color: #980020;
}

#sidebar-container.dark .theme-toggle:hover {
  background-color: rgba(255, 107, 107, 0.1);
  color: #ff6b6b;
}

.bx {
  font-size: 1.4rem;
  min-width: 24px;
}

.menu-text {
  transition: opacity 0.2s ease;
}

#sidebar-container {
  width: 0;
  overflow: hidden;
  transition: width 0.3s ease;
}

#sidebar-container.mobile:not(.collapsed) {
  width: 250px;
}

#sidebar-container.collapsed .menu-text {
  opacity: 0;
  width: 0;
  display: none;
}

#sidebar-container:not(.collapsed) .menu-text {
  opacity: 1;
  width: auto;
  display: inline;
}

/* TELAS GRANDES (desktop) */
@media (min-width: 768px) {
  #sidebar-container {
    width: 60px;
  }

  #sidebar-container:not(.collapsed) {
    width: 250px;
  }

  #sidebar-container.collapsed:hover {
    width: 250px;
  }

  #sidebar-container.collapsed:hover .menu-text {
    opacity: 1;
    width: auto;
    display: inline;
  }

  .chevron-icon {
    display: block;
  }

  .mobile-menu-icon {
    display: none;
  }
}

@media (max-width: 1490px) {
  #sidebar-container {
    width: 100px;
  }
  
  #sidebar-container:not(.collapsed) {
    width: 250px;
  }
  
  .chevron-icon {
    display: none;
  }
  
  .mobile-menu-icon {
    display: block;
  }
}

@media (min-width: 375px) {
  #sidebar-container {
    width: 60px;
  }
  
  #sidebar-container:not(.collapsed) {
    width: 250px;
  }
  
  .chevron-icon {
    display: none;
  }
  
  .mobile-menu-icon {
    display: block;
  }
}
</style>