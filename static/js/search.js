document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('#show-card-form').addEventListener('click', event => {
    event.preventDefault()
    document.querySelector('#card-form').classList.remove('hide')
  })
})
