/*!
 * Color mode toggler for Bootstrap's docs (https://getbootstrap.com/)
 * Copyright 2011-2023 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */

(() => {
  'use strict'

  const getStoredTheme = () => localStorage.getItem('theme')
  const setStoredTheme = theme => localStorage.setItem('theme', theme)

  const getPreferredTheme = () => {
    const storedTheme = getStoredTheme()
    if (storedTheme) {
      return storedTheme
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  }

  const setTheme = theme => {
    document.documentElement.setAttribute('data-bs-theme', theme)
  }

  const updateSwitch = (theme) => {
    const themeSwitch = document.querySelector('#themeSwitch')
    const themeLabel = document.querySelector('#themeLabel')

    if (!themeSwitch || !themeLabel) {
      return
    }

    themeSwitch.checked = theme === 'dark'
    themeLabel.textContent = theme === 'dark' ? 'Dark Mode' : 'Light Mode'
  }

  setTheme(getPreferredTheme())
  updateSwitch(getPreferredTheme())

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    const storedTheme = getStoredTheme()
    if (!storedTheme) {
      setTheme(getPreferredTheme())
      updateSwitch(getPreferredTheme())
    }
  })

  window.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#themeSwitch').addEventListener('change', (event) => {
      const theme = event.target.checked ? 'dark' : 'light'
      setStoredTheme(theme)
      setTheme(theme)
      updateSwitch(theme)
    })
  })
})()
