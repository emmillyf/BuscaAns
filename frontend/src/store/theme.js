import { reactive } from 'vue'

const state = reactive({
  isDark: localStorage.getItem('theme') === 'dark'
})

const applyThemeClass = () => {
  if (state.isDark) {
    document.body.classList.add('dark-mode')
  } else {
    document.body.classList.remove('dark-mode')
  }
}

const toggleTheme = () => {
  state.isDark = !state.isDark
  localStorage.setItem('theme', state.isDark ? 'dark' : 'light')
  applyThemeClass()
}

applyThemeClass() 

export default function useTheme() {
  return {
    state,
    toggleTheme
  }
}
