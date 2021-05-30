/*
 highcharts JS v9.1.0 (2021-05-03)

 (c) 2009-2021 Torstein Honsi

 License: www.highcharts.com/license
*/
(function(c){"object"===typeof module&&module.exports?(c["default"]=c,module.exports=c):"function"===typeof define&&define.amd?define("highcharts/modules/broken-axis",["highcharts"],function(l){c(l);c.Highcharts=l;return c}):c("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(c){function l(c,l,w,k){c.hasOwnProperty(l)||(c[l]=k.apply(null,w))}c=c?c._modules:{};l(c,"Core/Axis/BrokenAxis.js",[c["Core/Axis/Axis.js"],c["Core/Series/Series.js"],c["Extensions/Stacking.js"],c["Core/Utilities.js"]],
function(c,l,w,k){var t=k.addEvent,A=k.find,z=k.fireEvent,B=k.isArray,n=k.isNumber,u=k.pick,C=function(){function m(b){this.hasBreaks=!1;this.axis=b}m.isInBreak=function(b,e){var d=b.repeat||Infinity,a=b.from,f=b.to-b.from;e=e>=a?(e-a)%d:d-(a-e)%d;return b.inclusive?e<=f:e<f&&0!==e};m.lin2Val=function(b){var e=this.brokenAxis;e=e&&e.breakArray;if(!e||!n(b))return b;var d;for(d=0;d<e.length;d++){var a=e[d];if(a.from>=b)break;else a.to<b?b+=a.len:m.isInBreak(a,b)&&(b+=a.len)}return b};m.val2Lin=function(b){var e=
this.brokenAxis;e=e&&e.breakArray;if(!e||!n(b))return b;var d=b,a;for(a=0;a<e.length;a++){var f=e[a];if(f.to<=b)d-=f.len;else if(f.from>=b)break;else if(m.isInBreak(f,b)){d-=b-f.from;break}}return d};m.prototype.findBreakAt=function(b,e){return A(e,function(d){return d.from<b&&b<d.to})};m.prototype.isInAnyBreak=function(b,e){var d=this.axis,a=d.options.breaks||[],f=a.length,x;if(f&&n(b)){for(;f--;)if(m.isInBreak(a[f],b)){var v=!0;x||(x=u(a[f].showPoints,!d.isXAxis))}var c=v&&e?v&&!x:v}return c};m.prototype.setBreaks=
function(b,e){var d=this,a=d.axis,f=B(b)&&!!b.length;a.isDirty=d.hasBreaks!==f;d.hasBreaks=f;a.options.breaks=a.userOptions.breaks=b;a.forceRedraw=!0;a.series.forEach(function(a){a.isDirty=!0});f||a.val2lin!==m.val2Lin||(delete a.val2lin,delete a.lin2val);f&&(a.userOptions.ordinal=!1,a.lin2val=m.lin2Val,a.val2lin=m.val2Lin,a.setExtremes=function(a,b,f,g,e){if(d.hasBreaks){for(var h,v=this.options.breaks;h=d.findBreakAt(a,v);)a=h.to;for(;h=d.findBreakAt(b,v);)b=h.from;b<a&&(b=a)}c.prototype.setExtremes.call(this,
a,b,f,g,e)},a.setAxisTranslation=function(){c.prototype.setAxisTranslation.call(this);d.unitLength=void 0;if(d.hasBreaks){var b=a.options.breaks||[],f=[],e=[],g=0,q,h=a.userMin||a.min,r=a.userMax||a.max,l=u(a.pointRangePadding,0),k;b.forEach(function(a){q=a.repeat||Infinity;n(h)&&n(r)&&(m.isInBreak(a,h)&&(h+=a.to%q-h%q),m.isInBreak(a,r)&&(r-=r%q-a.from%q))});b.forEach(function(a){p=a.from;q=a.repeat||Infinity;if(n(h)&&n(r)){for(;p-q>h;)p-=q;for(;p<h;)p+=q;for(k=p;k<r;k+=q)f.push({value:k,move:"in"}),
f.push({value:k+a.to-a.from,move:"out",size:a.breakSize})}});f.sort(function(a,b){return a.value===b.value?("in"===a.move?0:1)-("in"===b.move?0:1):a.value-b.value});var y=0;var p=h;f.forEach(function(a){y+="in"===a.move?1:-1;1===y&&"in"===a.move&&(p=a.value);0===y&&n(p)&&(e.push({from:p,to:a.value,len:a.value-p-(a.size||0)}),g+=a.value-p-(a.size||0))});d.breakArray=e;n(h)&&n(r)&&n(a.min)&&(d.unitLength=r-h-g+l,z(a,"afterBreaks"),a.staticScale?a.transA=a.staticScale:d.unitLength&&(a.transA*=(r-a.min+
l)/d.unitLength),l&&(a.minPixelPadding=a.transA*(a.minPointOffset||0)),a.min=h,a.max=r)}});u(e,!0)&&a.chart.redraw()};return m}();k=function(){function c(){}c.compose=function(b,e){b.keepProps.push("brokenAxis");var d=l.prototype;d.drawBreaks=function(a,b){var f=this,e=f.points,d,g,c,h;if(a&&a.brokenAxis&&a.brokenAxis.hasBreaks){var k=a.brokenAxis;b.forEach(function(b){d=k&&k.breakArray||[];g=a.isXAxis?a.min:u(f.options.threshold,a.min);e.forEach(function(f){h=u(f["stack"+b.toUpperCase()],f[b]);d.forEach(function(b){if(n(g)&&
n(h)){c=!1;if(g<b.from&&h>b.to||g>b.from&&h<b.from)c="pointBreak";else if(g<b.from&&h>b.from&&h<b.to||g>b.from&&h>b.to&&h<b.from)c="pointInBreak";c&&z(a,c,{point:f,brk:b})}})})})}};d.gappedPath=function(){var a=this.currentDataGrouping,b=a&&a.gapSize;a=this.options.gapSize;var e=this.points.slice(),d=e.length-1,c=this.yAxis,g;if(a&&0<d)for("value"!==this.options.gapUnit&&(a*=this.basePointRange),b&&b>a&&b>=this.basePointRange&&(a=b),g=void 0;d--;)g&&!1!==g.visible||(g=e[d+1]),b=e[d],!1!==g.visible&&
!1!==b.visible&&(g.x-b.x>a&&(g=(b.x+g.x)/2,e.splice(d+1,0,{isNull:!0,x:g}),c.stacking&&this.options.stacking&&(g=c.stacking.stacks[this.stackKey][g]=new w(c,c.options.stackLabels,!1,g,this.stack),g.total=0)),g=b);return this.getGraphPath(e)};t(b,"init",function(){this.brokenAxis||(this.brokenAxis=new C(this))});t(b,"afterInit",function(){"undefined"!==typeof this.brokenAxis&&this.brokenAxis.setBreaks(this.options.breaks,!1)});t(b,"afterSetTickPositions",function(){var a=this.brokenAxis;if(a&&a.hasBreaks){var b=
this.tickPositions,e=this.tickPositions.info,d=[],c;for(c=0;c<b.length;c++)a.isInAnyBreak(b[c])||d.push(b[c]);this.tickPositions=d;this.tickPositions.info=e}});t(b,"afterSetOptions",function(){this.brokenAxis&&this.brokenAxis.hasBreaks&&(this.options.ordinal=!1)});t(e,"afterGeneratePoints",function(){var a=this.options.connectNulls,b=this.points,c=this.xAxis,d=this.yAxis;if(this.isDirty)for(var e=b.length;e--;){var g=b[e],k=!(null===g.y&&!1===a)&&(c&&c.brokenAxis&&c.brokenAxis.isInAnyBreak(g.x,!0)||
d&&d.brokenAxis&&d.brokenAxis.isInAnyBreak(g.y,!0));g.visible=k?!1:!1!==g.options.visible}});t(e,"afterRender",function(){this.drawBreaks(this.xAxis,["x"]);this.drawBreaks(this.yAxis,u(this.pointArrayMap,["y"]))})};return c}();k.compose(c,l);return k});l(c,"masters/modules/broken-axis.src.js",[],function(){})});
//# sourceMappingURL=broken-axis.js.map