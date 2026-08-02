'use strict';
const map=L.map('map').setView([23.7,120.95],7);
const base=L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:20,attribution:'© OpenStreetMap'}).addTo(map);
const photo=L.tileLayer('https://wmts.nlsc.gov.tw/wmts/PHOTO2/default/GoogleMapsCompatible/{z}/{y}/{x}',{maxZoom:20,opacity:.95});
const cadastral=L.tileLayer('https://wmts.nlsc.gov.tw/wmts/LANDSECT/default/GoogleMapsCompatible/{z}/{y}/{x}',{maxZoom:20,opacity:.72}).addTo(map);
const sites=L.layerGroup().addTo(map),drawn=new L.FeatureGroup().addTo(map),samples=new L.FeatureGroup().addTo(map),photos=new L.FeatureGroup().addTo(map);
map.addControl(new L.Control.Draw({edit:{featureGroup:drawn},draw:{marker:false,circlemarker:false}}));
map.on(L.Draw.Event.CREATED,e=>{drawn.addLayer(e.layer);updateCounts()});
let centerMarker, pendingPhotoLatLng;

function setCenter(lat,lng,title){
  if(centerMarker)centerMarker.setLatLng([lat,lng]);else centerMarker=L.marker([lat,lng]).addTo(map);
  centerMarker.bindPopup(title||'查詢位置');
  map.setView([lat,lng],18);
  queryTitle.textContent=title||'查詢位置';
  queryCoords.textContent=`${lat.toFixed(6)}, ${lng.toFixed(6)}`;
}
function updateCounts(){sampleCount.textContent=samples.getLayers().length;photoCount.textContent=photos.getLayers().length;shapeCount.textContent=drawn.getLayers().length}
async function geocode(address){
  const r=await fetch(`https://nominatim.openstreetmap.org/search?format=json&countrycodes=tw&limit=1&q=${encodeURIComponent(address)}`,{headers:{'Accept-Language':'zh-TW'}});
  const rows=await r.json(); if(!rows.length)throw new Error('找不到地址');
  return {lat:+rows[0].lat,lng:+rows[0].lon,label:rows[0].display_name}
}
document.querySelectorAll('.tabs button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.tabs button').forEach(x=>x.classList.remove('active'));document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));b.classList.add('active');document.querySelector('#'+b.dataset.tab).classList.add('active')});
addressBtn.onclick=async()=>{try{const q=await geocode(addressInput.value.trim());setCenter(q.lat,q.lng,q.label)}catch(e){alert(e.message)}};
parcelBtn.onclick=()=>{const title=`${county.value}${district.value}${section.value}${parcelNo.value}地號`;queryTitle.textContent=title;queryCoords.textContent='已建立地號查詢案件；請用地圖中心定位或 GPS/地址定位'};
gpsBtn.onclick=()=>navigator.geolocation.getCurrentPosition(p=>setCenter(p.coords.latitude,p.coords.longitude,'GPS 所在位置'),e=>alert(e.message),{enableHighAccuracy:true});
photoLayer.onchange=e=>e.target.checked?photo.addTo(map):map.removeLayer(photo);
cadastralLayer.onchange=e=>e.target.checked?cadastral.addTo(map):map.removeLayer(cadastral);
sitesLayer.onchange=e=>e.target.checked?sites.addTo(map):map.removeLayer(sites);
centerBtn.onclick=()=>{const c=map.getCenter();setCenter(c.lat,c.lng,'地圖中心位置')};
sampleBtn.onclick=()=>{
  const c=map.getCenter(),code=`S${String(samples.getLayers().length+1).padStart(2,'0')}`;
  const medium=sampleMedium.value,depth=sampleDepth.value||'待定',analysis=sampleAnalysis.value||'待確認';
  const m=L.marker(c,{draggable:true});
  m.feature={type:'Feature',properties:{kind:'sample',code,medium,depth,analysis}};
  m.bindPopup(`<b>採樣點 ${code}</b><br>介質：${medium}<br>深度：${depth}<br>分析：${analysis}`);
  samples.addLayer(m);updateCounts()
};
photoBtn.onclick=()=>{pendingPhotoLatLng=map.getCenter();photoInput.click()};
photoInput.onchange=e=>{const f=e.target.files[0];if(!f)return;const reader=new FileReader();reader.onload=()=>{const html=`<b>現勘照片</b><br><img class="photo-preview" src="${reader.result}"><br><span class="small">${new Date().toLocaleString()}</span>`;photos.addLayer(L.circleMarker(pendingPhotoLatLng,{radius:8}).bindPopup(html));updateCounts()};reader.readAsDataURL(f);e.target.value=''};
const rules=[
 {name:'金屬表面處理／電鍍',keys:['電鍍','表面處理','酸洗','鍍鉻','鍍鎳'],poll:['鉻','六價鉻','鎳','銅','鋅','鉛','鎘','氰化物'],analysis:['土壤重金屬','地下水重金屬','六價鉻','氰化物']},
 {name:'加油站／油品儲存',keys:['加油站','汽油','柴油','油槽','儲油'],poll:['TPH','BTEX','MTBE','PAHs'],analysis:['TPH','VOCs','PAHs']},
 {name:'乾洗業',keys:['乾洗','四氯乙烯','PCE'],poll:['PCE','TCE','DCE','VC'],analysis:['土壤氣體VOCs','土壤VOCs','地下水VOCs']},
 {name:'印刷／溶劑使用',keys:['印刷','油墨','溶劑','清洗劑'],poll:['VOCs','SVOCs','重金屬'],analysis:['VOCs','SVOCs','重金屬']},
 {name:'半導體／電子製造',keys:['半導體','晶圓','PCB','電路板','蝕刻'],poll:['VOCs','酸鹼','重金屬','含氟物質'],analysis:['VOCs','重金屬','氟鹽','依製程追加PFAS']}
];
assessBtn.onclick=()=>{const text=(business.value+' '+keywords.value).toLowerCase();const matched=rules.filter(r=>r.keys.some(k=>text.includes(k.toLowerCase())));if(!matched.length){assessment.innerHTML='資料不足，無法判定。請補充實際製程、原物料、化學品、許可及土地移轉／設立／停歇業情境。';return}
const names=matched.map(x=>`<span class="badge">${x.name}</span>`).join('');
const poll=[...new Set(matched.flatMap(x=>x.poll))].join('、');const ana=[...new Set(matched.flatMap(x=>x.analysis))].join('、');
assessment.innerHTML=`<b>可能符合公告事業：</b><br>${names}<br><b>潛勢污染物：</b>${poll}<br><b>建議分析：</b>${ana}<br><span class="small">此為系統初判，不取代依法辦理的評估調查與主管機關認定。</span>`};
function layerToFeature(l){
  const f=l.toGeoJSON();
  if(l.feature?.properties)f.properties={...(f.properties||{}),...l.feature.properties};
  return f;
}
function allGeoJSON(){return {type:'FeatureCollection',features:[...drawn.getLayers(),...samples.getLayers(),...photos.getLayers()].map(layerToFeature)}}
exportBtn.onclick=()=>{const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify(allGeoJSON(),null,2)],{type:'application/geo+json'}));a.download='soil-gis-field-plan.geojson';a.click();URL.revokeObjectURL(a.href)};
saveBtn.onclick=()=>{
  localStorage.setItem('soil_gis_case',JSON.stringify({
    projectName:projectName.value,clientName:clientName.value,projectNote:projectNote.value,
    title:queryTitle.textContent,coords:queryCoords.textContent,geojson:allGeoJSON()
  }));alert('已儲存到此瀏覽器')
};
loadBtn.onclick=()=>{
  const raw=localStorage.getItem('soil_gis_case');if(!raw)return alert('沒有儲存紀錄');
  const d=JSON.parse(raw);projectName.value=d.projectName||'';clientName.value=d.clientName||'';projectNote.value=d.projectNote||'';
  queryTitle.textContent=d.title;queryCoords.textContent=d.coords;
  L.geoJSON(d.geojson,{onEachFeature:(f,l)=>{
    if(f.properties?.kind==='sample'){l.feature=f;l.bindPopup(`<b>採樣點 ${f.properties.code||''}</b><br>介質：${f.properties.medium||''}<br>深度：${f.properties.depth||''}<br>分析：${f.properties.analysis||''}`);samples.addLayer(l)}
    else drawn.addLayer(l)
  }});updateCounts()
};
clearBtn.onclick=()=>{drawn.clearLayers();samples.clearLayers();photos.clearLayers();sites.clearLayers();updateCounts();nearestSite.textContent='尚未分析鄰近污染場址'};
function haversine(a,b){
  const R=6371000,toRad=x=>x*Math.PI/180;
  const dLat=toRad(b.lat-a.lat),dLng=toRad(b.lng-a.lng);
  const q=Math.sin(dLat/2)**2+Math.cos(toRad(a.lat))*Math.cos(toRad(b.lat))*Math.sin(dLng/2)**2;
  return 2*R*Math.asin(Math.sqrt(q))
}
function analyzeNearestSite(){
  if(!centerMarker||!sites.getLayers().length){nearestSite.textContent='尚無足夠資料分析';return}
  const c=centerMarker.getLatLng();let best=null;
  sites.eachLayer(l=>{if(!l.getLatLng)return;const d=haversine(c,l.getLatLng());if(!best||d<best.d)best={d,l}});
  if(best)nearestSite.textContent=`最近污染場址約 ${(best.d/1000).toFixed(2)} 公里`
}
siteFile.onchange=async e=>{
  const f=e.target.files[0];if(!f)return;sites.clearLayers();
  if(f.name.toLowerCase().endsWith('.csv')){
    const text=await f.text();const rows=text.split(/\r?\n/).filter(Boolean);const head=rows.shift().split(',');
    const latI=head.findIndex(x=>/lat|緯度/i.test(x)),lngI=head.findIndex(x=>/lng|lon|經度/i.test(x)),nameI=head.findIndex(x=>/name|名稱|場址/i.test(x));
    let n=0;for(const row of rows){const c=row.split(',');const lat=+c[latI],lng=+c[lngI];if(Number.isFinite(lat)&&Number.isFinite(lng)){L.circleMarker([lat,lng],{radius:6}).bindPopup(c[nameI]||'污染場址').addTo(sites);n++}}
    syncStatus.textContent=`已載入 ${n} 筆 CSV 場址資料・${new Date().toLocaleString()}`
  }else{
    const gj=JSON.parse(await f.text());
    L.geoJSON(gj,{pointToLayer:(f,ll)=>L.circleMarker(ll,{radius:6}),onEachFeature:(f,l)=>l.bindPopup(f.properties?.name||f.properties?.場址名稱||'污染場址')}).addTo(sites);
    syncStatus.textContent=`已載入 GeoJSON・${new Date().toLocaleString()}`
  }
  analyzeNearestSite()
};
siteUpdated.textContent=new Date().toLocaleString();
updateCounts();

function updateConnectivity() {
  offlineBanner.hidden = navigator.onLine;
}
window.addEventListener('online', updateConnectivity);
window.addEventListener('offline', updateConnectivity);
updateConnectivity();
if ('serviceWorker' in navigator && location.protocol !== 'file:') {
  window.addEventListener('load', () => navigator.serviceWorker.register('./sw.js'));
}
