/*
 highcharts JS v9.1.0 (2021-05-03)

 Boost module

 (c) 2010-2021 Highsoft AS
 Author: Torstein Honsi

 License: www.highcharts.com/license
*/
(function(c){"object"===typeof module&&module.exports?(c["default"]=c,module.exports=c):"function"===typeof define&&define.amd?define("highcharts/modules/boost-canvas",["highcharts"],function(g){c(g);c.Highcharts=g;return c}):c("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(c){function g(c,g,v,B){c.hasOwnProperty(g)||(c[g]=B.apply(null,v))}c=c?c._modules:{};g(c,"Extensions/BoostCanvas.js",[c["Core/Chart/Chart.js"],c["Core/Color/Color.js"],c["Core/Globals.js"],c["Core/Color/Palette.js"],
c["Core/Series/Series.js"],c["Core/Series/SeriesRegistry.js"],c["Core/Utilities.js"]],function(c,g,v,B,C,D,r){var ea=g.parse,E=v.doc,fa=v.noop,m=D.seriesTypes,F=r.addEvent,y=r.extend,ha=r.fireEvent,ia=r.isNumber,ja=r.merge,ka=r.pick,z=r.wrap,P;return function(){v.seriesTypes.heatmap&&z(v.seriesTypes.heatmap.prototype,"drawPoints",function(){var a=this.chart,b=this.getContext(),f=this.chart.inverted,c=this.xAxis,d=this.yAxis;b?(this.points.forEach(function(e){var k=e.plotY;if("undefined"!==typeof k&&
!isNaN(k)&&null!==e.y&&b){var l=e.shapeArgs||{};k=l.x;k=void 0===k?0:k;var g=l.y;g=void 0===g?0:g;var u=l.width;u=void 0===u?0:u;l=l.height;l=void 0===l?0:l;e=a.styledMode?e.series.colorAttribs(e):e.series.pointAttribs(e);b.fillStyle=e.fill;f?b.fillRect(d.len-g+c.left,c.len-k+d.top,-l,-u):b.fillRect(k+c.left,g+d.top,u,l)}}),this.canvasToSVG()):this.chart.showLoading("Your browser doesn't support HTML5 canvas, <br>please use a modern browser")});y(C.prototype,{getContext:function(){var a=this.chart,
b=a.chartWidth,f=a.chartHeight,c=a.seriesGroup||this.group,d=this,g=function(a,d,f,b,c,e,g){a.call(this,f,d,b,c,e,g)};a.isChartSeriesBoosting()&&(d=a,c=a.seriesGroup);var k=d.ctx;d.canvas||(d.canvas=E.createElement("canvas"),d.renderTarget=a.renderer.image("",0,0,b,f).addClass("highcharts-boost-canvas").add(c),d.ctx=k=d.canvas.getContext("2d"),a.inverted&&["moveTo","lineTo","rect","arc"].forEach(function(a){z(k,a,g)}),d.boostCopy=function(){d.renderTarget.attr({href:d.canvas.toDataURL("image/png")})},
d.boostClear=function(){k.clearRect(0,0,d.canvas.width,d.canvas.height);d===this&&d.renderTarget.attr({href:""})},d.boostClipRect=a.renderer.clipRect(),d.renderTarget.clip(d.boostClipRect));d.canvas.width!==b&&(d.canvas.width=b);d.canvas.height!==f&&(d.canvas.height=f);d.renderTarget.attr({x:0,y:0,width:b,height:f,style:"pointer-events: none",href:""});d.boostClipRect.attr(a.getBoostClipRect(d));return k},canvasToSVG:function(){this.chart.isChartSeriesBoosting()?this.boostClear&&this.boostClear():
(this.boostCopy||this.chart.boostCopy)&&(this.boostCopy||this.chart.boostCopy)()},cvsLineTo:function(a,b,f){a.lineTo(b,f)},renderCanvas:function(){var a=this,b=a.options,f=a.chart,c=this.xAxis,d=this.yAxis,m=(f.options.boost||{}).timeRendering||!1,k=0,l=a.processedXData,z=a.processedYData,u=b.data,n=c.getExtremes(),G=n.min,H=n.max;n=d.getExtremes();var C=n.min,D=n.max,Q={},I,E=!!a.sampling,J=b.marker&&b.marker.radius,R=this.cvsDrawPoint,K=b.lineWidth?this.cvsLineTo:void 0,S=J&&1>=J?this.cvsMarkerSquare:
this.cvsMarkerCircle,la=this.cvsStrokeBatch||1E3,ma=!1!==b.enableMouseTracking,T;n=b.threshold;var w=d.getThreshold(n),U=ia(n),V=w,na=this.fill,W=a.pointArrayMap&&"low,high"===a.pointArrayMap.join(","),X=!!b.stacking,Y=a.cropStart||0;n=f.options.loading;var oa=a.requireSorting,Z,pa=b.connectNulls,aa=!l,L,M,x,A,N,t=X?a.data:l||u,qa=a.fillOpacity?(new g(a.color)).setOpacity(ka(b.fillOpacity,.75)).get():a.color,ba=function(){na?(p.fillStyle=qa,p.fill()):(p.strokeStyle=a.color,p.lineWidth=b.lineWidth,
p.stroke())},ca=function(d,b,c,e){0===k&&(p.beginPath(),K&&(p.lineJoin="round"));f.scroller&&"highcharts-navigator-series"===a.options.className?(b+=f.scroller.top,c&&(c+=f.scroller.top)):b+=f.plotTop;d+=f.plotLeft;Z?p.moveTo(d,b):R?R(p,d,b,c,T):K?K(p,d,b):S&&S.call(a,p,d,b,J,e);k+=1;k===la&&(ba(),k=0);T={clientX:d,plotY:b,yBottom:c}},ra="x"===b.findNearestPointBy,da=this.xData||this.options.xData||this.processedXData||!1,O=function(a,b,e){N=ra?a:a+","+b;ma&&!Q[N]&&(Q[N]=!0,f.inverted&&(a=c.len-a,
b=d.len-b),sa.push({x:da?da[Y+e]:!1,clientX:a,plotX:a,plotY:b,i:Y+e}))};this.renderTarget&&this.renderTarget.attr({href:""});(this.points||this.graph)&&this.destroyGraphics();a.plotGroup("group","series",a.visible?"visible":"hidden",b.zIndex,f.seriesGroup);a.markerGroup=a.group;F(a,"destroy",function(){a.markerGroup=null});var sa=this.points=[];var p=this.getContext();a.buildKDTree=fa;this.boostClear&&this.boostClear();this.visible&&(99999<u.length&&(f.options.loading=ja(n,{labelStyle:{backgroundColor:ea(B.backgroundColor).setOpacity(.75).get(),
padding:"1em",borderRadius:"0.5em"},style:{backgroundColor:"none",opacity:1}}),r.clearTimeout(P),f.showLoading("Drawing..."),f.options.loading=n),m&&console.time("canvas rendering"),v.eachAsync(t,function(b,e){var g=!1,k=!1,l=!1,m=!1,n="undefined"===typeof f.index,p=!0;if(!n){if(aa){var q=b[0];var h=b[1];t[e+1]&&(l=t[e+1][0]);t[e-1]&&(m=t[e-1][0])}else q=b,h=z[e],t[e+1]&&(l=t[e+1]),t[e-1]&&(m=t[e-1]);l&&l>=G&&l<=H&&(g=!0);m&&m>=G&&m<=H&&(k=!0);if(W){aa&&(h=b.slice(1,3));var r=h[0];h=h[1]}else X&&
(q=b.x,h=b.stackY,r=h-b.y);b=null===h;oa||(p=h>=C&&h<=D);if(!b&&(q>=G&&q<=H&&p||g||k))if(q=Math.round(c.toPixels(q,!0)),E){if("undefined"===typeof x||q===I){W||(r=h);if("undefined"===typeof A||h>M)M=h,A=e;if("undefined"===typeof x||r<L)L=r,x=e}q!==I&&("undefined"!==typeof x&&(h=d.toPixels(M,!0),w=d.toPixels(L,!0),ca(q,U?Math.min(h,V):h,U?Math.max(w,V):w,e),O(q,h,A),w!==h&&O(q,w,x)),x=A=void 0,I=q)}else h=Math.round(d.toPixels(h,!0)),ca(q,h,w,e),O(q,h,e);Z=b&&!pa;0===e%5E4&&(a.boostCopy||a.chart.boostCopy)&&
(a.boostCopy||a.chart.boostCopy)()}return!n},function(){var b=f.loadingDiv,d=f.loadingShown;ba();a.canvasToSVG();m&&console.timeEnd("canvas rendering");ha(a,"renderedCanvas");d&&(y(b.style,{transition:"opacity 250ms",opacity:0}),f.loadingShown=!1,P=setTimeout(function(){b.parentNode&&b.parentNode.removeChild(b);f.loadingDiv=f.loadingSpan=null},250));delete a.buildKDTree;a.buildKDTree()},f.renderer.forExport?Number.MAX_VALUE:void 0))}});m.scatter.prototype.cvsMarkerCircle=function(a,b,c,e){a.moveTo(b,
c);a.arc(b,c,e,0,2*Math.PI,!1)};m.scatter.prototype.cvsMarkerSquare=function(a,b,c,e){a.rect(b-e,c-e,2*e,2*e)};m.scatter.prototype.fill=!0;m.bubble&&(m.bubble.prototype.cvsMarkerCircle=function(a,b,c,e,d){a.moveTo(b,c);a.arc(b,c,this.radii&&this.radii[d],0,2*Math.PI,!1)},m.bubble.prototype.cvsStrokeBatch=1);y(m.area.prototype,{cvsDrawPoint:function(a,b,c,e,d){d&&b!==d.clientX&&(a.moveTo(d.clientX,d.yBottom),a.lineTo(d.clientX,d.plotY),a.lineTo(b,c),a.lineTo(b,e))},fill:!0,fillOpacity:!0,sampling:!0});
y(m.column.prototype,{cvsDrawPoint:function(a,b,c,e){a.rect(b-1,c,1,e-c)},fill:!0,sampling:!0});c.prototype.callbacks.push(function(a){F(a,"predraw",function(){a.renderTarget&&a.renderTarget.attr({href:""});a.canvas&&a.canvas.getContext("2d").clearRect(0,0,a.canvas.width,a.canvas.height)});F(a,"render",function(){a.boostCopy&&a.boostCopy()})})}});g(c,"masters/modules/boost-canvas.src.js",[],function(){})});
//# sourceMappingURL=boost-canvas.js.map