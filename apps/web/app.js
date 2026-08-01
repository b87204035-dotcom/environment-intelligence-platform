const API = `${location.protocol}//${location.hostname}:8000`;
const map = L.map('map').setView([23.7,120.95],7);
const base = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:20,attribution:'© OpenStreetMap'}).addTo(map);
const photo = L.tileLayer('https://wmts.nlsc.gov.tw/wmts/PHOTO2/default/GoogleMapsCompatible/{z}/{y}/{x}',{maxZoom:20,opacity:.95});
const cadastral = L.tileLayer('https://wmts.nlsc.gov.tw/wmts/LANDSECT/default/GoogleMapsCompatible/{z}/{y}/{x}',{maxZoom:20,opacity:.7}).addTo(map);
const sites = L.layerGroup().addTo(map);
const drawn = new L.FeatureGroup().addTo(map);
const samples = new L.FeatureGroup().addTo(map);
const photos = new L.FeatureGroup().addTo(map);
map.addControl(new L.Control.Draw({edit:{featureGroup:drawn},draw:{marker:false,circlemarker:false}}));
map.on(L.Draw.Event.CREATED,e=>{drawn.addLayer(e.layer); updateCounts();});

let centerMarker;
function setCenter(lat,lng,title){
  if(centerMarker) centerMarker.setLatLng([lat,lng]); else centerMarker=L.marker([lat,lng]).addTo(map);
  map.setView([lat,lng],18); document.querySelector('#queryTitle').textContent=title; document.querySelector('#queryCoords').textContent=`${lat.toFixed(6)}, ${lng.toFixed(6)}`;
}
function updateCounts(){
  document.querySelector('#sampleCount').textContent=samples.getLayers().length;
  document.querySelector('#photoCount').textContent=photos.getLayers().length;
  document.querySelector('#shapeCount').textContent=drawn.getLayers().length;
}
async function geocode(address){
  const url=`https://nominatim.openstreetmap.org/search?format=json&limit=1&q=${encodeURIComponent(address)}`;
  const r=await fetch(url,{headers:{'Accept-Language':'zh-TW'}}); const rows=await r.json();
  if(!rows.length) throw new Error('找不到地址'); return {lat:+rows[0].lat,lng:+rows[0].lon,label:rows[0].display_name};
}

document.querySelectorAll('.tabs button').forEach(b=>b.onclick=()=>{
  document.querySelectorAll('.tabs button').forEach(x=>x.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));
  b.classList.add('active'); document.querySelector(`#${b.dataset.tab}`).classList.add('active');
});
document.querySelector('#addressBtn').onclick=async()=>{try{const q=await geocode(document.querySelector('#addressInput').value);setCenter(q.lat,q.lng,q.label);}catch(e){alert(e.message)}};
document.querySelector('#parcelBtn').onclick=async()=>{
  const payload={mode:'parcel',county:county.value,district:district.value,section:section.value,parcel_no:parcelNo.value};
  const r=await fetch(`${API}/v1/location/resolve`,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(payload)}); const data=await r.json();
  document.querySelector('#queryTitle').textContent=`${county.value}${district.value}${section.value}${parcelNo.value}地號`;
  document.querySelector('#queryCoords').textContent=data.message;
};
document.querySelector('#gpsBtn').onclick=()=>navigator.geolocation.getCurrentPosition(p=>setCenter(p.coords.latitude,p.coords.longitude,'GPS 所在位置'),e=>alert(e.message),{enableHighAccuracy:true});
document.querySelector('#photoLayer').onchange=e=>e.target.checked?photo.addTo(map):map.removeLayer(photo);
document.querySelector('#cadastralLayer').onchange=e=>e.target.checked?cadastral.addTo(map):map.removeLayer(cadastral);
document.querySelector('#sitesLayer').onchange=e=>e.target.checked?sites.addTo(map):map.removeLayer(sites);
document.querySelector('#centerBtn').onclick=()=>{const c=map.getCenter();setCenter(c.lat,c.lng,'地圖中心位置')};
document.querySelector('#sampleBtn').onclick=()=>{const c=map.getCenter();const code=`S${String(samples.getLayers().length+1).padStart(2,'0')}`;samples.addLayer(L.marker(c,{draggable:true}).bindPopup(`採樣點 ${code}`));updateCounts();};
document.querySelector('#photoBtn').onclick=()=>{const c=map.getCenter();photos.addLayer(L.circleMarker(c,{radius:7}).bindPopup('現勘照片位置'));updateCounts();};
document.querySelector('#assessBtn').onclick=async()=>{
  const terms=keywords.value.split(/[、,，\n]/).map(x=>x.trim()).filter(Boolean);
  const r=await fetch(`${API}/v1/regulations/articles-8-9/assess`,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({business_name:business.value,industry_keywords:terms,processes:[],chemicals:[]})});
  const d=await r.json(); document.querySelector('#assessment').innerHTML=`判定：${d.classification}<br>第8條：${d.article_8}<br>第9條：${d.article_9}<br><small>${d.legal_disclaimer}</small>`;
};
document.querySelector('#exportBtn').onclick=()=>{
  const collection={type:'FeatureCollection',features:[...drawn.getLayers(),...samples.getLayers(),...photos.getLayers()].map(l=>l.toGeoJSON())};
  const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify(collection,null,2)],{type:'application/geo+json'}));a.download='eip-field-plan.geojson';a.click();URL.revokeObjectURL(a.href);
};
fetch(`${API}/health`).then(r=>r.json()).then(()=>apiStatus.textContent='API 正常').catch(()=>apiStatus.textContent='API 尚未連線');
updateCounts();
