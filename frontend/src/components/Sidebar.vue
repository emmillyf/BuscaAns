<!-- <template>

    <div id="container" :class="{ 'dark': isDark }">
        <div id="sidebar"> 
            <div id="user-area">
                <i class='bx bxs-user-circle'>
                <p class="user" style='color:black'>{{ userName }}</p></i>
                <i class='bx bx-chevron-right chevron-icon'/>
             </div>
        </div>
        <div id="menu">
                <ul>
                    <li v-for="item in firstItems" :key="item.id" class="first-item">
                         <i :class="'bx ' + item.icon">{{ item.text }}</i>
                    </li>
                    <div class="flex-gap"/>
                    <li v-for="item in dynamicLastItems" :key="item.id" :class="['last-item', item.specialClass]"
                    @click="item.id === 4 ? toggleDarkMode() : null">
                        <i :class="'bx ' + item.icon">{{ item.text }}</i>
                    </li>
                </ul> 
            </div>  
    </div >

</template>

<script>
// import IconUser from '@/components/Icons/UserIcon.vue'
export default {
  name: 'AppSidebar',
//   components: { IconUser}, 
  data() {
    return {
    userName: 'Nome do Usuário',
    firstItems: [
        { id: 1, icon: 'bx-home-alt-2', text: 'Início' }
      ],
      lastItems: [
        { id: 2, icon: 'bx-export', text: 'Exportar CSV' },
        { id: 3, icon: 'bx-log-out', text: 'Logout' },
        { id: 4, icon: 'bx-moon'}
      ],
    }
  },
};
</script>

<style scoped>

*{
    font-family: "Poppins", sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.theme-toggle {
  background: none;
  border: none;
  cursor: pointer;
  color: var(--text-color);
  font-size: 1.2rem;
  margin-left: 10px;
}

#container{
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 250px;
    padding: 10px 14px;
    background: #DDD;
}

:root {

    --body-color: #E4E9F7;
    --sidebar-color: #FFF;
    --primary-color: #C3203E;
    --primary-color-light: #fff5f5;
    --toggle-color: #ffbbaf;
    --text-color: #707070;

    --tran-02: all 0.2s ease;
    --tran-03: all 0.3s ease;
    --tran-04: all 0.4s ease;
    --tran-05: all 0.5s ease;
}

#user-area{
    position: relative;
}

#user-area .user{
    font-size: 1.4rem;
    font-weight: 500;
}

#user-area .bxs-user-circle {
    display: flex;
    padding: 20px 20px;
    align-items: center;
    gap: 12px;
    font-size: 40px; 
    color: #980020;
    flex-shrink: 0; 
}

#user-area .chevron-icon {  
  position: absolute;
  top:50%;
  right: -25px;
  transform: translateY(-50%);
  height: 25px;
  width: 25px;
  background: #980020;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: white;
  font-size: 20px;
}

.first-item {
   display: flex;
}

.flex-gap {
  flex: 1;
  min-height: 250px;
}

.last-item {
  padding: 12px 20px;
  margin: 4px 0;
}

#menu .mode-type{
    display: flex;
    align-items: center;
    gap: 13px;
    font-size: 1.2rem; 
    font-weight: 300;
    color: var(--text-color);
}

#menu{
    /* background: yellow; */
    height: 100%;
}

#menu ul {
    top: 50%;
    align-items: center; 
    list-style: none;
    padding: 10px 0;
}

#menu li {
    height: 50px;
    margin-top: 10px;
    list-style: none;
    align-items: center;
    padding: 10px 0;
}

#menu li i {
    display: flex;
    align-items: center;
    gap: 13px;
    font-size: 1.2rem; 
    font-weight: 300;
    color: var(--text-color);
}

</style> -->