import {GIFEncoder} from 'gifenc';
import {jsPDF} from 'jspdf';

// Browser port of ant.ai's local experiments, not a security boundary.
// New canvas/PRNG outputs are not byte-identical to the earlier Python trials.
let active=null, urls=[];
const fontReady=new FontFace('AntVera','url(./fonts/VeraBd.ttf)').load().then(f=>document.fonts.add(f));
function random(n){const a=new Uint32Array(1);crypto.getRandomValues(a);return a[0]%n;}
function canvas(w,h){const c=document.createElement('canvas');c.width=w;c.height=h;return c;}
function mask(text,w,h,size=110,left=false){
 const c=canvas(w,h),x=c.getContext('2d',{willReadFrequently:true});
 do{x.font=`${size--}px AntVera`;}while(x.measureText(text).width>w-70&&size>20);
 x.textAlign=left?'left':'center';x.textBaseline='alphabetic';
 const metrics=x.measureText(text),above=metrics.actualBoundingBoxAscent,below=metrics.actualBoundingBoxDescent;
 x.fillStyle='white';x.fillText(text,left?26:w/2,(h+above-below)/2);
 return x.getImageData(0,0,w,h).data;
}
function stripes(text,pitch){
 const c=canvas(1000,240),x=c.getContext('2d'),m=mask(text,c.width,c.height),out=x.createImageData(c.width,c.height),phase=random(pitch);
 for(let y=0;y<c.height;y++)for(let xx=0;xx<c.width;xx++){
  const i=(y*c.width+xx)*4,a=m[i+3]/255,bg=(y+phase)%pitch<pitch/2?35:255,fg=(xx+phase)%pitch<pitch/2?35:255,v=Math.round(bg*(1-a)+fg*a);
  out.data[i]=out.data[i+1]=out.data[i+2]=v;out.data[i+3]=255;
 }x.putImageData(out,0,0);return c;
}
function dots(text){
 const c=canvas(1032,126),x=c.getContext('2d'),m=mask(text,c.width,c.height,76,true);
 const fg=[[192,179,108],[107,122,91],[207,201,161],[99,93,56],[167,144,84],[158,159,131]],bg=[[248,175,96],[249,113,71],[244,80,51],[228,87,62]];
 x.fillStyle='#f6f3ec';x.fillRect(0,0,c.width,c.height);
 for(let row=0,y=-7;y<c.height+7;y+=7,row++)for(let xx=-7;xx<c.width+7;xx+=7){
  const px=xx+(row%2?3.5:0)+(random(160)/100-.8),py=y+(random(160)/100-.8),mx=Math.max(0,Math.min(c.width-1,Math.round(px))),my=Math.max(0,Math.min(c.height-1,Math.round(py)));
  const palette=m[(my*c.width+mx)*4+3]>128?fg:bg,v=palette[random(palette.length)],j=random(11)-5;
  x.fillStyle=`rgb(${v.map(n=>n+j).join(',')})`;x.beginPath();x.arc(px,py,2.5+random(110)/100,0,Math.PI*2);x.fill();
 }return c;
}
function links(){
 const c=canvas(1224,1584),x=c.getContext('2d'),names=['Cedar','Harbor','Orchid','Quartz','Willow','Juniper','Maple','Amber','Birch','Aspen'];
 for(let i=names.length-1;i>0;i--){const j=random(i+1);[names[i],names[j]]=[names[j],names[i]];}
 const chosen=names.slice(0,5),codes=[];while(codes.length<5){const code='KEY-'+(10000+random(89999));if(!codes.includes(code))codes.push(code);}
 const swaps=Array.from({length:4},()=>random(4)),ends=[0,1,2,3,4],ys=[440,600,760,920,1080],xs=[370,478,586,694,802];
 for(const s of swaps)for(let i=0;i<5;i++){if(ends[i]===s)ends[i]=s+1;else if(ends[i]===s+1)ends[i]=s;}
 x.fillStyle='white';x.fillRect(0,0,c.width,c.height);x.fillStyle='#182833';
 x.font='39px AntVera';x.fillText('ant.ai / connection experiment',80,100);x.font='25px AntVera';
 x.fillText('Follow each workshop’s line to its code.',80,240);x.fillText('At a crossing, continue straight. Do not turn.',80,285);
 x.font='23px AntVera';x.fillText('WORKSHOP',80,355);x.fillText('ACCESS CODE',865,355);
 const line=(a,b,d,e,color='#182833',width=5)=>{x.strokeStyle=color;x.lineWidth=width;x.beginPath();x.moveTo(a,b);x.lineTo(d,e);x.stroke();};
 for(let i=0;i<5;i++){x.font='32px AntVera';x.fillText(chosen[i],80,ys[i]+10);x.font='30px AntVera';x.fillText(codes[i],865,ys[i]+10);line(345,ys[i],xs[0],ys[i]);line(xs[4],ys[i],825,ys[i]);}
 for(let j=0;j<4;j++){const s=swaps[j];for(let k=0;k<5;k++)if(k!==s&&k!==s+1)line(xs[j],ys[k],xs[j+1],ys[k]);line(xs[j],ys[s],xs[j+1],ys[s+1]);line(xs[j],ys[s+1],xs[j+1],ys[s],'white',15);line(xs[j],ys[s+1],xs[j+1],ys[s]);}
 x.font='24px AntVera';x.fillStyle='#182833';x.fillText('All codes are visible. Only the connections are tested.',80,1280);
 return {image:c,answer:Object.fromEntries(chosen.map((n,i)=>[n,codes[ends[i]]]))};
}
const blobURL=blob=>{const u=URL.createObjectURL(blob);urls.push(u);return u;};
const png=c=>new Promise((resolve,reject)=>c.toBlob(b=>b?resolve(b):reject(Error('Could not create the image.')),'image/png'));
async function motion(text){
 const w=640,h=160,c=canvas(w,h),x=c.getContext('2d'),m=mask(text,w,h,62),fg=new Uint8Array(w*h),bg=new Uint8Array(w*h);
 crypto.getRandomValues(fg.subarray(0,65536));crypto.getRandomValues(fg.subarray(65536));crypto.getRandomValues(bg.subarray(0,65536));crypto.getRandomValues(bg.subarray(65536));
 const gif=GIFEncoder(),palette=[[0,0,0],[255,255,255]],rgba=x.createImageData(w,h);let first;
 for(let t=0;t<48;t++){
  const indices=new Uint8Array(w*h);
  for(let y=0;y<h;y++)for(let xx=0;xx<w;xx++){const p=y*w+xx,inside=m[p*4+3]>127,row=inside?(y+2*t)%h:(y-2*t+h*2)%h,v=(inside?fg:bg)[row*w+xx]&1;indices[p]=v;rgba.data[p*4]=rgba.data[p*4+1]=rgba.data[p*4+2]=v*255;rgba.data[p*4+3]=255;}
  if(t===0){x.putImageData(rgba,0,0);first=await png(c);}
  gif.writeFrame(indices,w,h,{palette,delay:40,repeat:0});
  if(t%8===0)await new Promise(requestAnimationFrame);
 }gif.finish();return {preview:blobURL(first),animated:blobURL(new Blob([gif.bytes()],{type:'image/gif'}))};
}
export async function localApi(action,payload){
 if(action==='reveal'){if(!active||active.id!==payload.id)throw Error('Make a new challenge first.');return {answer:active.answer};}
 if(action!=='create')throw Error('Unsupported action.');
 await fontReady;
 const alphabet='ABCDEFGHJKMNPQRSTUVWXYZ23456789';
 const mode=payload.mode,pitch=payload.pitch,text=payload.text.trim().replace(/\s+/g,' ')||Array.from({length:6},()=>alphabet[random(alphabet.length)]).join('');
 if(!['stripes','dots','motion','links'].includes(mode)||!Number.isInteger(pitch)||pitch<4||pitch>16)throw Error('Choose a valid method and stripe spacing.');
 if(mode!=='links'&&(text.length>(mode==='motion'?14:36)||/[^\x20-\x7e]/.test(text)))throw Error('Use short English text, digits or basic punctuation.');
 const oldUrls=urls;urls=[];let image,answer=text,result;
 try{
  if(mode==='motion'){result=await motion(text);result.downloads={'challenge.png':result.preview,'challenge.gif':result.animated};}
  else{
   if(mode==='stripes')image=stripes(text,pitch);else if(mode==='dots')image=dots(text);else{const v=links();image=v.image;answer=v.answer;}
   const preview=blobURL(await png(image)),w=image.width,h=image.height;
   const pdf=new jsPDF({orientation:w>=h?'landscape':'portrait',unit:'pt',format:[w,h],compress:true});pdf.setProperties({title:'ant.ai visual experiment'});pdf.addImage(image.toDataURL('image/png'),'PNG',0,0,w,h);
   result={preview,animated:null,downloads:{'challenge.png':preview,'challenge.pdf':blobURL(pdf.output('blob'))}};
  }
 }catch(error){urls.forEach(u=>URL.revokeObjectURL(u));urls=oldUrls;throw error;}
 oldUrls.forEach(u=>URL.revokeObjectURL(u));
 active={id:crypto.randomUUID(),answer};return {...result,id:active.id,notice:'Ready. Download it or take a screenshot to try with AI.'};
}
