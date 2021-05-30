/*
 highcharts JS v9.1.0 (2021-05-03)

 Dependency wheel module

 (c) 2010-2021 Torstein Honsi

 License: www.highcharts.com/license
*/
(function(b){"object"===typeof module&&module.exports?(b["default"]=b,module.exports=b):"function"===typeof define&&define.amd?define("highcharts/modules/dependency-wheel",["highcharts","highcharts/modules/sankey"],function(d){b(d);b.Highcharts=d;return b}):b("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(b){function d(b,h,a,d){b.hasOwnProperty(h)||(b[h]=d.apply(null,a))}b=b?b._modules:{};d(b,"Series/DependencyWheel/DependencyWheelPoint.js",[b["Mixins/Nodes.js"],b["Core/Series/SeriesRegistry.js"],
b["Core/Utilities.js"]],function(b,h,a){var d=this&&this.__extends||function(){var b=function(a,e){b=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(b,e){b.__proto__=e}||function(b,e){for(var a in e)e.hasOwnProperty(a)&&(b[a]=e[a])};return b(a,e)};return function(a,e){function g(){this.constructor=a}b(a,e);a.prototype=null===e?Object.create(e):(g.prototype=e.prototype,new g)}}();a=a.extend;h=function(b){function a(){var a=null!==b&&b.apply(this,arguments)||this;a.angle=void 0;a.fromNode=
void 0;a.index=void 0;a.linksFrom=void 0;a.linksTo=void 0;a.options=void 0;a.series=void 0;a.shapeArgs=void 0;a.toNode=void 0;return a}d(a,b);a.prototype.getDataLabelPath=function(b){var a=this.series.chart.renderer,e=this.shapeArgs,d=0>this.angle||this.angle>Math.PI,p=e.start||0,q=e.end||0;this.dataLabelPath||(this.dataLabelPath=a.arc({open:!0,longArc:Math.abs(Math.abs(p)-Math.abs(q))<Math.PI?0:1}).add(b));this.dataLabelPath.attr({x:e.x,y:e.y,r:e.r+(this.dataLabel.options.distance||0),start:d?p:
q,end:d?q:p,clockwise:+d});return this.dataLabelPath};a.prototype.isValid=function(){return!0};return a}(h.seriesTypes.sankey.prototype.pointClass);a(h.prototype,{setState:b.setNodeState});return h});d(b,"Series/DependencyWheel/DependencyWheelSeries.js",[b["Core/Animation/AnimationUtilities.js"],b["Series/DependencyWheel/DependencyWheelPoint.js"],b["Core/Globals.js"],b["Core/Series/SeriesRegistry.js"],b["Core/Utilities.js"]],function(b,d,a,r,g){var h=this&&this.__extends||function(){var b=function(a,
f){b=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(b,a){b.__proto__=a}||function(b,a){for(var f in a)a.hasOwnProperty(f)&&(b[f]=a[f])};return b(a,f)};return function(a,f){function k(){this.constructor=a}b(a,f);a.prototype=null===f?Object.create(f):(k.prototype=f.prototype,new k)}}(),e=b.animObject,t=a.deg2rad;a=r.seriesTypes;b=a.pie;var n=a.sankey;a=g.extend;var u=g.merge;g=function(b){function a(){var a=null!==b&&b.apply(this,arguments)||this;a.data=void 0;a.options=void 0;a.nodeColumns=
void 0;a.nodes=void 0;a.points=void 0;return a}h(a,b);a.prototype.animate=function(a){if(!a){var b=e(this.options.animation).duration/2/this.nodes.length;this.nodes.forEach(function(a,k){var e=a.graphic;e&&(e.attr({opacity:0}),setTimeout(function(){a.graphic&&a.graphic.animate({opacity:1},{duration:b})},b*k))},this);this.points.forEach(function(a){var b=a.graphic;!a.isNode&&b&&b.attr({opacity:0}).animate({opacity:1},this.options.animation)},this)}};a.prototype.createNode=function(a){var b=n.prototype.createNode.call(this,
a);b.index=this.nodes.length-1;b.getSum=function(){return b.linksFrom.concat(b.linksTo).reduce(function(a,b){return a+b.weight},0)};b.offset=function(a){function e(a){return a.fromNode===b?a.toNode:a.fromNode}var f=0,c,d=b.linksFrom.concat(b.linksTo);d.sort(function(a,b){return e(a).index-e(b).index});for(c=0;c<d.length;c++)if(e(d[c]).index>b.index){d=d.slice(0,c).reverse().concat(d.slice(c).reverse());var k=!0;break}k||d.reverse();for(c=0;c<d.length;c++){if(d[c]===a)return f;f+=d[c].weight}};return b};
a.prototype.createNodeColumns=function(){var a=[this.createNodeColumn()];this.nodes.forEach(function(b){b.column=0;a[0].push(b)});return a};a.prototype.getNodePadding=function(){return this.options.nodePadding/Math.PI};a.prototype.translate=function(){var a=this.options,b=2*Math.PI/(this.chart.plotHeight+this.getNodePadding()),d=this.getCenter(),e=(a.startAngle-90)*t;n.prototype.translate.call(this);this.nodeColumns[0].forEach(function(f){if(f.sum){var c=f.shapeArgs,g=d[0],h=d[1],k=d[2]/2,l=k-a.nodeWidth,
m=e+b*(c.y||0);c=e+b*((c.y||0)+(c.height||0));f.angle=m+(c-m)/2;f.shapeType="arc";f.shapeArgs={x:g,y:h,r:k,innerR:l,start:m,end:c};f.dlBox={x:g+Math.cos((m+c)/2)*(k+l)/2,y:h+Math.sin((m+c)/2)*(k+l)/2,width:1,height:1};f.linksFrom.forEach(function(d){if(d.linkBase){var f,c=d.linkBase.map(function(c,k){c*=b;var m=Math.cos(e+c)*(l+1),n=Math.sin(e+c)*(l+1),p=a.curveFactor;f=Math.abs(d.linkBase[3-k]*b-c);f>Math.PI&&(f=2*Math.PI-f);f*=l;f<l&&(p*=f/l);return{x:g+m,y:h+n,cpX:g+(1-p)*m,cpY:h+(1-p)*n}});d.shapeArgs=
{d:[["M",c[0].x,c[0].y],["A",l,l,0,0,1,c[1].x,c[1].y],["C",c[1].cpX,c[1].cpY,c[2].cpX,c[2].cpY,c[2].x,c[2].y],["A",l,l,0,0,1,c[3].x,c[3].y],["C",c[3].cpX,c[3].cpY,c[0].cpX,c[0].cpY,c[0].x,c[0].y]]}}})}})};a.defaultOptions=u(n.defaultOptions,{center:[null,null],curveFactor:.6,startAngle:0});return a}(n);a(g.prototype,{orderNodes:!1,getCenter:b.prototype.getCenter});g.prototype.pointClass=d;r.registerSeriesType("dependencywheel",g);"";return g});d(b,"masters/modules/dependency-wheel.src.js",[],function(){})});
//# sourceMappingURL=dependency-wheel.js.map