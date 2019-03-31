

export const getAll = () =>
  fetch()
    .then(res => res.json())
    .then(data => data.contacts)
