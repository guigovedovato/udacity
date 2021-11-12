import fetchGoogleMaps from 'fetch-google-maps';

var points = [
  {id: 1, title: 'Estádio Prof. Dr. José Vieira de Carvalho', location: {lat: 41.2344665, lng: -8.6181843}},
  {id: 2, title: 'Parque Urbano Novo Rumo', location: {lat: 41.2289127, lng: -8.6244071}},
  {id: 3, title: 'Fórum Da Maia', location: {lat: 41.2339727, lng: -8.6231866}},
  {id: 4, title: 'Jardim das Pirâmides', location: {lat: 41.2321334, lng: -8.6272651}},
  {id: 5, title: 'Zoo da Maia', location: {lat: 41.2335485, lng: -8.6302851}}
];

export const getAll = () => points
export const getMaps = () => {
  return fetchGoogleMaps({
    apiKey: '',
    language: 'en'
  }).catch((e) => console.log(e))
}

window.gm_authFailure = () => {
  alert("Unfortunately there was an error to load Google Maps!")
}
