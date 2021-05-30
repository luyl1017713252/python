/*
 highcharts JS v9.1.0 (2021-05-03)

 (c) 2014-2021 Highsoft AS
 Authors: Jon Arild Nygard / Oystein Moseng

 License: www.highcharts.com/license
*/
(function(a){"object"===typeof module&&module.exports?(a["default"]=a,module.exports=a):"function"===typeof define&&define.amd?define("highcharts/modules/treemap",["highcharts"],function(n){a(n);a.Highcharts=n;return a}):a("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(a){function n(a,e,c,t){a.hasOwnProperty(e)||(a[e]=t.apply(null,c))}a=a?a._modules:{};n(a,"Mixins/ColorMapSeries.js",[a["Core/Globals.js"],a["Core/Series/Point.js"],a["Core/Utilities.js"]],function(a,e,c){var t=c.defined;
c=c.addEvent;var g=a.noop;a=a.seriesTypes;c(e,"afterSetState",function(a){this.moveToTopOnHover&&this.graphic&&this.graphic.attr({zIndex:a&&"hover"===a.state?1:0})});return{colorMapPointMixin:{dataLabelOnNull:!0,moveToTopOnHover:!0,isValid:function(){return null!==this.value&&Infinity!==this.value&&-Infinity!==this.value}},colorMapSeriesMixin:{pointArrayMap:["value"],axisTypes:["xAxis","yAxis","colorAxis"],trackerGroups:["group","markerGroup","dataLabelsGroup"],getSymbol:g,parallelArrays:["x","y",
"value"],colorKey:"value",pointAttribs:a.column.prototype.pointAttribs,colorAttribs:function(a){var c={};t(a.color)&&(c[this.colorProp||"fill"]=a.color);return c}}}});n(a,"Series/Treemap/TreemapAlgorithmGroup.js",[],function(){return function(){function a(a,c,t,g){this.height=a;this.width=c;this.plot=g;this.startDirection=this.direction=t;this.lH=this.nH=this.lW=this.nW=this.total=0;this.elArr=[];this.lP={total:0,lH:0,nH:0,lW:0,nW:0,nR:0,lR:0,aspectRatio:function(a,c){return Math.max(a/c,c/a)}}}a.prototype.addElement=
function(a){this.lP.total=this.elArr[this.elArr.length-1];this.total+=a;0===this.direction?(this.lW=this.nW,this.lP.lH=this.lP.total/this.lW,this.lP.lR=this.lP.aspectRatio(this.lW,this.lP.lH),this.nW=this.total/this.height,this.lP.nH=this.lP.total/this.nW,this.lP.nR=this.lP.aspectRatio(this.nW,this.lP.nH)):(this.lH=this.nH,this.lP.lW=this.lP.total/this.lH,this.lP.lR=this.lP.aspectRatio(this.lP.lW,this.lH),this.nH=this.total/this.width,this.lP.nW=this.lP.total/this.nH,this.lP.nR=this.lP.aspectRatio(this.lP.nW,
this.nH));this.elArr.push(a)};a.prototype.reset=function(){this.lW=this.nW=0;this.elArr=[];this.total=0};return a}()});n(a,"Mixins/DrawPoint.js",[],function(){var a=function(a){return"function"===typeof a},e=function(c){var e=this,g=c.animatableAttribs,k=c.onComplete,r=c.css,l=c.renderer,m=this.series&&this.series.chart.hasRendered?void 0:this.series&&this.series.options.animation,b=this.graphic;if(this.shouldDraw())b||(this.graphic=b=l[c.shapeType](c.shapeArgs).add(c.group)),b.css(r).attr(c.attribs).animate(g,
c.isNew?!1:m,k);else if(b){var f=function(){e.graphic=b=b&&b.destroy();a(k)&&k()};Object.keys(g).length?b.animate(g,void 0,function(){f()}):f()}};return{draw:e,drawPoint:function(a){(a.attribs=a.attribs||{})["class"]=this.getClassName();e.call(this,a)},isFn:a}});n(a,"Series/Treemap/TreemapPoint.js",[a["Mixins/DrawPoint.js"],a["Core/Series/SeriesRegistry.js"],a["Core/Utilities.js"]],function(a,e,c){var t=this&&this.__extends||function(){var a=function(b,c){a=Object.setPrototypeOf||{__proto__:[]}instanceof
Array&&function(a,b){a.__proto__=b}||function(a,b){for(var f in b)b.hasOwnProperty(f)&&(a[f]=b[f])};return a(b,c)};return function(b,c){function f(){this.constructor=b}a(b,c);b.prototype=null===c?Object.create(c):(f.prototype=c.prototype,new f)}}(),g=e.series.prototype.pointClass,k=e.seriesTypes;e=k.pie.prototype.pointClass;var r=c.extend,l=c.isNumber,m=c.pick;c=function(a){function b(){var b=null!==a&&a.apply(this,arguments)||this;b.name=void 0;b.node=void 0;b.options=void 0;b.series=void 0;b.value=
void 0;return b}t(b,a);b.prototype.getClassName=function(){var a=g.prototype.getClassName.call(this),b=this.series,c=b.options;this.node.level<=b.nodeMap[b.rootNode].level?a+=" highcharts-above-level":this.node.isLeaf||m(c.interactByLeaf,!c.allowTraversingTree)?this.node.isLeaf||(a+=" highcharts-internal-node"):a+=" highcharts-internal-node-interactive";return a};b.prototype.isValid=function(){return!(!this.id&&!l(this.value))};b.prototype.setState=function(a){g.prototype.setState.call(this,a);this.graphic&&
this.graphic.attr({zIndex:"hover"===a?1:0})};b.prototype.shouldDraw=function(){return l(this.plotY)&&null!==this.y};return b}(k.scatter.prototype.pointClass);r(c.prototype,{draw:a.drawPoint,setVisible:e.prototype.setVisible});return c});n(a,"Series/Treemap/TreemapUtilities.js",[a["Core/Utilities.js"]],function(a){var e=a.objectEach,c;(function(a){function c(a,e,l){void 0===l&&(l=this);a=e.call(l,a);!1!==a&&c(a,e,l)}a.AXIS_MAX=100;a.isBoolean=function(a){return"boolean"===typeof a};a.eachObject=function(a,
c,l){l=l||this;e(a,function(m,b){c.call(l,m,b,a)})};a.recursive=c})(c||(c={}));return c});n(a,"Mixins/TreeSeries.js",[a["Core/Color/Color.js"],a["Core/Utilities.js"]],function(a,e){var c=e.extend,t=e.isArray,g=e.isNumber,k=e.isObject,r=e.merge,l=e.pick;return{getColor:function(c,b){var f=b.index,e=b.mapOptionsToLevel,m=b.parentColor,k=b.parentColorIndex,g=b.series,y=b.colors,t=b.siblings,q=g.points,r=g.chart.options.chart,w;if(c){q=q[c.i];c=e[c.level]||{};if(e=q&&c.colorByPoint){var n=q.index%(y?
y.length:r.colorCount);var D=y&&y[n]}if(!g.chart.styledMode){y=q&&q.options.color;r=c&&c.color;if(w=m)w=(w=c&&c.colorVariation)&&"brightness"===w.key?a.parse(m).brighten(f/t*w.to).get():m;w=l(y,r,D,w,g.color)}var F=l(q&&q.options.colorIndex,c&&c.colorIndex,n,k,b.colorIndex)}return{color:w,colorIndex:F}},getLevelOptions:function(a){var b=null;if(k(a)){b={};var f=g(a.from)?a.from:1;var e=a.levels;var l={};var m=k(a.defaults)?a.defaults:{};t(e)&&(l=e.reduce(function(a,b){if(k(b)&&g(b.level)){var e=r({},
b);var l="boolean"===typeof e.levelIsConstant?e.levelIsConstant:m.levelIsConstant;delete e.levelIsConstant;delete e.level;b=b.level+(l?0:f-1);k(a[b])?c(a[b],e):a[b]=e}return a},{}));e=g(a.to)?a.to:1;for(a=0;a<=e;a++)b[a]=r({},m,k(l[a])?l[a]:{})}return b},setTreeValues:function M(a,e){var b=e.before,f=e.idRoot,g=e.mapIdToNode[f],k=e.points[a.i],r=k&&k.options||{},q=0,n=[];a.levelDynamic=a.level-(("boolean"===typeof e.levelIsConstant?e.levelIsConstant:1)?0:g.level);a.name=l(k&&k.name,"");a.visible=
f===a.id||("boolean"===typeof e.visible?e.visible:!1);"function"===typeof b&&(a=b(a,e));a.children.forEach(function(b,f){var l=c({},e);c(l,{index:f,siblings:a.children.length,visible:a.visible});b=M(b,l);n.push(b);b.visible&&(q+=b.val)});a.visible=0<q||a.visible;b=l(r.value,q);a.children=n;a.childrenTotal=q;a.isLeaf=a.visible&&!q;a.val=b;return a},updateRootId:function(a){if(k(a)){var b=k(a.options)?a.options:{};b=l(a.rootNode,b.rootId,"");k(a.userOptions)&&(a.userOptions.rootId=b);a.rootNode=b}return b}}});
n(a,"Series/Treemap/TreemapComposition.js",[a["Core/Series/SeriesRegistry.js"],a["Series/Treemap/TreemapUtilities.js"],a["Core/Utilities.js"]],function(a,e,c){var n=c.addEvent,g=c.extend,k=!1;n(a.series,"afterBindAxes",function(){var a=this.xAxis,c=this.yAxis;if(a&&c)if(this.is("treemap")){var m={endOnTick:!1,gridLineWidth:0,lineWidth:0,min:0,minPadding:0,max:e.AXIS_MAX,maxPadding:0,startOnTick:!1,title:void 0,tickPositions:[]};g(c.options,m);g(a.options,m);k=!0}else k&&(c.setOptions(c.userOptions),
a.setOptions(a.userOptions),k=!1)})});n(a,"Series/Treemap/TreemapSeries.js",[a["Core/Color/Color.js"],a["Mixins/ColorMapSeries.js"],a["Core/Globals.js"],a["Mixins/LegendSymbol.js"],a["Core/Color/Palette.js"],a["Core/Series/SeriesRegistry.js"],a["Series/Treemap/TreemapAlgorithmGroup.js"],a["Series/Treemap/TreemapPoint.js"],a["Series/Treemap/TreemapUtilities.js"],a["Mixins/TreeSeries.js"],a["Core/Utilities.js"]],function(a,e,c,n,g,k,r,l,m,b,f){var t=this&&this.__extends||function(){var a=function(b,
d){a=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(d,a){d.__proto__=a}||function(d,a){for(var h in a)a.hasOwnProperty(h)&&(d[h]=a[h])};return a(b,d)};return function(b,d){function h(){this.constructor=b}a(b,d);b.prototype=null===d?Object.create(d):(h.prototype=d.prototype,new h)}}(),I=a.parse,J=e.colorMapSeriesMixin;a=c.noop;var B=k.series;e=k.seriesTypes;var y=e.column,F=e.heatmap,q=e.scatter,N=b.getColor,w=b.getLevelOptions,O=b.updateRootId,D=f.addEvent,P=f.correctFloat,C=f.defined,
Q=f.error,E=f.extend,R=f.fireEvent,K=f.isArray,S=f.isObject,G=f.isString,A=f.merge,x=f.pick,T=f.stableSort;b=function(a){function b(){var d=null!==a&&a.apply(this,arguments)||this;d.axisRatio=void 0;d.data=void 0;d.mapOptionsToLevel=void 0;d.nodeMap=void 0;d.options=void 0;d.points=void 0;d.rootNode=void 0;d.tree=void 0;return d}t(b,a);b.prototype.algorithmCalcPoints=function(d,a,b,c){var h,u,p,e,H=b.lW,v=b.lH,f=b.plot,k=0,l=b.elArr.length-1;if(a)H=b.nW,v=b.nH;else var g=b.elArr[b.elArr.length-1];
b.elArr.forEach(function(d){if(a||k<l)0===b.direction?(h=f.x,u=f.y,p=H,e=d/p):(h=f.x,u=f.y,e=v,p=d/e),c.push({x:h,y:u,width:p,height:P(e)}),0===b.direction?f.y+=e:f.x+=p;k+=1});b.reset();0===b.direction?b.width-=H:b.height-=v;f.y=f.parent.y+(f.parent.height-b.height);f.x=f.parent.x+(f.parent.width-b.width);d&&(b.direction=1-b.direction);a||b.addElement(g)};b.prototype.algorithmFill=function(d,a,b){var h=[],z,c=a.direction,p=a.x,e=a.y,f=a.width,v=a.height,k,l,g,m;b.forEach(function(b){z=b.val/a.val*
a.height*a.width;k=p;l=e;0===c?(m=v,g=z/m,f-=g,p+=g):(g=f,m=z/g,v-=m,e+=m);h.push({x:k,y:l,width:g,height:m});d&&(c=1-c)});return h};b.prototype.algorithmLowAspectRatio=function(a,b,c){var d=[],h=this,p,e={x:b.x,y:b.y,parent:b},f=0,g=c.length-1,v=new r(b.height,b.width,b.direction,e);c.forEach(function(c){p=c.val/b.val*b.height*b.width;v.addElement(p);v.lP.nR>v.lP.lR&&h.algorithmCalcPoints(a,!1,v,d,e);f===g&&h.algorithmCalcPoints(a,!0,v,d,e);f+=1});return d};b.prototype.alignDataLabel=function(a,
b,c){var d=c.style;d&&!C(d.textOverflow)&&b.text&&b.getBBox().width>b.text.textWidth&&b.css({textOverflow:"ellipsis",width:d.width+="px"});y.prototype.alignDataLabel.apply(this,arguments);a.dataLabel&&a.dataLabel.attr({zIndex:(a.node.zIndex||0)+1})};b.prototype.buildNode=function(a,b,c,e,z){var d=this,h=[],p=d.points[b],u=0,f;(e[a]||[]).forEach(function(b){f=d.buildNode(d.points[b].id,b,c+1,e,a);u=Math.max(f.height+1,u);h.push(f)});b={id:a,i:b,children:h,height:u,level:c,parent:z,visible:!1};d.nodeMap[b.id]=
b;p&&(p.node=b);return b};b.prototype.calculateChildrenAreas=function(a,b){var d=this,h=d.options,c=d.mapOptionsToLevel[a.level+1],e=x(d[c&&c.layoutAlgorithm]&&c.layoutAlgorithm,h.layoutAlgorithm),f=h.alternateStartingDirection,g=[];a=a.children.filter(function(a){return!a.ignore});c&&c.layoutStartingDirection&&(b.direction="vertical"===c.layoutStartingDirection?0:1);g=d[e](b,a);a.forEach(function(a,h){h=g[h];a.values=A(h,{val:a.childrenTotal,direction:f?1-b.direction:b.direction});a.pointValues=
A(h,{x:h.x/d.axisRatio,y:m.AXIS_MAX-h.y-h.height,width:h.width/d.axisRatio});a.children.length&&d.calculateChildrenAreas(a,a.values)})};b.prototype.drawDataLabels=function(){var a=this,b=a.mapOptionsToLevel,c,e;a.points.filter(function(a){return a.node.visible}).forEach(function(d){e=b[d.node.level];c={style:{}};d.node.isLeaf||(c.enabled=!1);e&&e.dataLabels&&(c=A(c,e.dataLabels),a._hasPointLabels=!0);d.shapeArgs&&(c.style.width=d.shapeArgs.width,d.dataLabel&&d.dataLabel.css({width:d.shapeArgs.width+
"px"}));d.dlOptions=A(c,d.options.dataLabels)});B.prototype.drawDataLabels.call(this)};b.prototype.drawPoints=function(){var a=this,b=a.chart,c=b.renderer,e=b.styledMode,f=a.options,U=e?{}:f.shadow,g=f.borderRadius,k=b.pointCount<f.animationLimit,l=f.allowTraversingTree;a.points.forEach(function(d){var b=d.node.levelDynamic,h={},p={},z={},u="level-group-"+d.node.level,L=!!d.graphic,m=k&&L,n=d.shapeArgs;d.shouldDraw()&&(d.isInside=!0,g&&(p.r=g),A(!0,m?h:p,L?n:{},e?{}:a.pointAttribs(d,d.selected?"select":
void 0)),a.colorAttribs&&e&&E(z,a.colorAttribs(d)),a[u]||(a[u]=c.g(u).attr({zIndex:1E3-(b||0)}).add(a.group),a[u].survive=!0));d.draw({animatableAttribs:h,attribs:p,css:z,group:a[u],renderer:c,shadow:U,shapeArgs:n,shapeType:"rect"});l&&d.graphic&&(d.drillId=f.interactByLeaf?a.drillToByLeaf(d):a.drillToByGroup(d))})};b.prototype.drillToByGroup=function(a){var d=!1;1!==a.node.level-this.nodeMap[this.rootNode].level||a.node.isLeaf||(d=a.id);return d};b.prototype.drillToByLeaf=function(a){var d=!1;if(a.node.parent!==
this.rootNode&&a.node.isLeaf)for(a=a.node;!d;)a=this.nodeMap[a.parent],a.parent===this.rootNode&&(d=a.id);return d};b.prototype.drillToNode=function(a,b){Q(32,!1,void 0,{"treemap.drillToNode":"use treemap.setRootNode"});this.setRootNode(a,b)};b.prototype.drillUp=function(){var a=this.nodeMap[this.rootNode];a&&G(a.parent)&&this.setRootNode(a.parent,!0,{trigger:"traverseUpButton"})};b.prototype.getExtremes=function(){var a=B.prototype.getExtremes.call(this,this.colorValueData),b=a.dataMax;this.valueMin=
a.dataMin;this.valueMax=b;return B.prototype.getExtremes.call(this)};b.prototype.getListOfParents=function(a,b){a=K(a)?a:[];var d=K(b)?b:[];b=a.reduce(function(a,b,d){b=x(b.parent,"");"undefined"===typeof a[b]&&(a[b]=[]);a[b].push(d);return a},{"":[]});m.eachObject(b,function(a,b,c){""!==b&&-1===d.indexOf(b)&&(a.forEach(function(a){c[""].push(a)}),delete c[b])});return b};b.prototype.getTree=function(){var a=this.data.map(function(a){return a.id});a=this.getListOfParents(this.data,a);this.nodeMap=
{};return this.buildNode("",-1,0,a)};b.prototype.hasData=function(){return!!this.processedXData.length};b.prototype.init=function(a,b){J&&(this.colorAttribs=J.colorAttribs);var d=D(this,"setOptions",function(a){a=a.userOptions;C(a.allowDrillToNode)&&!C(a.allowTraversingTree)&&(a.allowTraversingTree=a.allowDrillToNode,delete a.allowDrillToNode);C(a.drillUpButton)&&!C(a.traverseUpButton)&&(a.traverseUpButton=a.drillUpButton,delete a.drillUpButton)});B.prototype.init.call(this,a,b);delete this.opacity;
this.eventsToUnbind.push(d);this.options.allowTraversingTree&&this.eventsToUnbind.push(D(this,"click",this.onClickDrillToNode))};b.prototype.onClickDrillToNode=function(a){var b=(a=a.point)&&a.drillId;G(b)&&(a.setState(""),this.setRootNode(b,!0,{trigger:"click"}))};b.prototype.pointAttribs=function(a,b){var d=S(this.mapOptionsToLevel)?this.mapOptionsToLevel:{},c=a&&d[a.node.level]||{};d=this.options;var e=b&&d.states[b]||{},h=a&&a.getClassName()||"";a={stroke:a&&a.borderColor||c.borderColor||e.borderColor||
d.borderColor,"stroke-width":x(a&&a.borderWidth,c.borderWidth,e.borderWidth,d.borderWidth),dashstyle:a&&a.borderDashStyle||c.borderDashStyle||e.borderDashStyle||d.borderDashStyle,fill:a&&a.color||this.color};-1!==h.indexOf("highcharts-above-level")?(a.fill="none",a["stroke-width"]=0):-1!==h.indexOf("highcharts-internal-node-interactive")?(b=x(e.opacity,d.opacity),a.fill=I(a.fill).setOpacity(b).get(),a.cursor="pointer"):-1!==h.indexOf("highcharts-internal-node")?a.fill="none":b&&(a.fill=I(a.fill).brighten(e.brightness).get());
return a};b.prototype.renderTraverseUpButton=function(a){var b=this,d=b.options.traverseUpButton,c=x(d.text,b.nodeMap[a].name,"\u25c1 Back");if(""===a||b.is("sunburst")&&1===b.tree.children.length&&a===b.tree.children[0].id)b.drillUpButton&&(b.drillUpButton=b.drillUpButton.destroy());else if(this.drillUpButton)this.drillUpButton.placed=!1,this.drillUpButton.attr({text:c}).align();else{var e=(a=d.theme)&&a.states;this.drillUpButton=this.chart.renderer.button(c,0,0,function(){b.drillUp()},a,e&&e.hover,
e&&e.select).addClass("highcharts-drillup-button").attr({align:d.position.align,zIndex:7}).add().align(d.position,!1,d.relativeTo||"plotBox")}};b.prototype.setColorRecursive=function(a,b,c,e,f){var d=this,h=d&&d.chart;h=h&&h.options&&h.options.colors;if(a){var g=N(a,{colors:h,index:e,mapOptionsToLevel:d.mapOptionsToLevel,parentColor:b,parentColorIndex:c,series:d,siblings:f});if(b=d.points[a.i])b.color=g.color,b.colorIndex=g.colorIndex;(a.children||[]).forEach(function(b,c){d.setColorRecursive(b,g.color,
g.colorIndex,c,a.children.length)})}};b.prototype.setPointValues=function(){var a=this,b=a.xAxis,c=a.yAxis,e=a.chart.styledMode;a.points.forEach(function(d){var h=d.node,f=h.pointValues;h=h.visible;if(f&&h){h=f.height;var g=f.width,k=f.x,l=f.y,p=e?0:(a.pointAttribs(d)["stroke-width"]||0)%2/2;f=Math.round(b.toPixels(k,!0))-p;g=Math.round(b.toPixels(k+g,!0))-p;k=Math.round(c.toPixels(l,!0))-p;h=Math.round(c.toPixels(l+h,!0))-p;h={x:Math.min(f,g),y:Math.min(k,h),width:Math.abs(g-f),height:Math.abs(h-
k)};d.plotX=h.x+h.width/2;d.plotY=h.y+h.height/2;d.shapeArgs=h}else delete d.plotX,delete d.plotY})};b.prototype.setRootNode=function(a,b,c){a=E({newRootId:a,previousRootId:this.rootNode,redraw:x(b,!0),series:this},c);R(this,"setRootNode",a,function(a){var b=a.series;b.idPreviousRoot=a.previousRootId;b.rootNode=a.newRootId;b.isDirty=!0;a.redraw&&b.chart.redraw()})};b.prototype.setState=function(a){this.options.inactiveOtherPoints=!0;B.prototype.setState.call(this,a,!1);this.options.inactiveOtherPoints=
!1};b.prototype.setTreeValues=function(a){var b=this,d=b.options,c=b.nodeMap[b.rootNode];d=m.isBoolean(d.levelIsConstant)?d.levelIsConstant:!0;var e=0,f=[],g=b.points[a.i];a.children.forEach(function(a){a=b.setTreeValues(a);f.push(a);a.ignore||(e+=a.val)});T(f,function(a,b){return(a.sortIndex||0)-(b.sortIndex||0)});var k=x(g&&g.options.value,e);g&&(g.value=k);E(a,{children:f,childrenTotal:e,ignore:!(x(g&&g.visible,!0)&&0<k),isLeaf:a.visible&&!e,levelDynamic:a.level-(d?0:c.level),name:x(g&&g.name,
""),sortIndex:x(g&&g.sortIndex,-k),val:k});return a};b.prototype.sliceAndDice=function(a,b){return this.algorithmFill(!0,a,b)};b.prototype.squarified=function(a,b){return this.algorithmLowAspectRatio(!0,a,b)};b.prototype.strip=function(a,b){return this.algorithmLowAspectRatio(!1,a,b)};b.prototype.stripes=function(a,b){return this.algorithmFill(!1,a,b)};b.prototype.translate=function(){var a=this,b=a.options,c=O(a);B.prototype.translate.call(a);var e=a.tree=a.getTree();var f=a.nodeMap[c];""===c||f&&
f.children.length||(a.setRootNode("",!1),c=a.rootNode,f=a.nodeMap[c]);a.renderTraverseUpButton(c);a.mapOptionsToLevel=w({from:f.level+1,levels:b.levels,to:e.height,defaults:{levelIsConstant:a.options.levelIsConstant,colorByPoint:b.colorByPoint}});m.recursive(a.nodeMap[a.rootNode],function(b){var c=!1,d=b.parent;b.visible=!0;if(d||""===d)c=a.nodeMap[d];return c});m.recursive(a.nodeMap[a.rootNode].children,function(a){var b=!1;a.forEach(function(a){a.visible=!0;a.children.length&&(b=(b||[]).concat(a.children))});
return b});a.setTreeValues(e);a.axisRatio=a.xAxis.len/a.yAxis.len;a.nodeMap[""].pointValues=c={x:0,y:0,width:m.AXIS_MAX,height:m.AXIS_MAX};a.nodeMap[""].values=c=A(c,{width:c.width*a.axisRatio,direction:"vertical"===b.layoutStartingDirection?0:1,val:e.val});a.calculateChildrenAreas(e,c);a.colorAxis||b.colorByPoint||a.setColorRecursive(a.tree);b.allowTraversingTree&&(b=f.pointValues,a.xAxis.setExtremes(b.x,b.x+b.width,!1),a.yAxis.setExtremes(b.y,b.y+b.height,!1),a.xAxis.setScale(),a.yAxis.setScale());
a.setPointValues()};b.defaultOptions=A(q.defaultOptions,{allowTraversingTree:!1,animationLimit:250,showInLegend:!1,marker:void 0,colorByPoint:!1,dataLabels:{defer:!1,enabled:!0,formatter:function(){var a=this&&this.point?this.point:{};return G(a.name)?a.name:""},inside:!0,verticalAlign:"middle"},tooltip:{headerFormat:"",pointFormat:"<b>{point.name}</b>: {point.value}<br/>"},ignoreHiddenPoint:!0,layoutAlgorithm:"sliceAndDice",layoutStartingDirection:"vertical",alternateStartingDirection:!1,levelIsConstant:!0,
drillUpButton:{position:{align:"right",x:-10,y:10}},traverseUpButton:{position:{align:"right",x:-10,y:10}},borderColor:g.neutralColor10,borderWidth:1,colorKey:"colorValue",opacity:.15,states:{hover:{borderColor:g.neutralColor40,brightness:F?0:.1,halo:!1,opacity:.75,shadow:!1}}});return b}(q);E(b.prototype,{buildKDTree:a,colorKey:"colorValue",directTouch:!0,drawLegendSymbol:n.drawRectangle,getExtremesFromAll:!0,getSymbol:a,optionalAxis:"colorAxis",parallelArrays:["x","y","value","colorValue"],pointArrayMap:["value"],
pointClass:l,trackerGroups:["group","dataLabelsGroup"],utils:{recursive:m.recursive}});k.registerSeriesType("treemap",b);"";return b});n(a,"masters/modules/treemap.src.js",[],function(){})});
//# sourceMappingURL=treemap.js.map