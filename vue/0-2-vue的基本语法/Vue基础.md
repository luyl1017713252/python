### Vue基础

es6的语法

let 的特点 1.局部作用域 2.不会存在变量提升的问题 3.变量不能重复声明

const 的特点 1.局部作用域 2.不会存在变量提升问题
            3.变量不能重复声明 4.是一个常量不能重新赋值

### 模板字符串

​    let name = '杨凡'
​    let str = `我是${name}`

### es6的箭头函数

let add2 = (x, y) => {
        return x + y;
    }

### es6的对象

let person3 = {
        name: '杨凡',
        fav() {
            console.log(this)
        }
    }
    person3.fav()

### es6类的定义

class Person {
        constructor(name = '曾洲', age = 18) {
            this.name = name;
            this.age = age;
        }
        showName(){
            console.log(this.name)
        }
    }

## Vue的基本语法

### 1、创建Vue对象

new Vue({
        el: '#app',// 绑定需要操作的元素
        data: {
            msg: '曾洲',
            person:{
                name:'杨凡'
            },
            m2:'hello Vue',
            text:'<h2>下班了</h2>'
        }
    })

### 2、模板语法

    <h2>{{ msg }}</h2>
    <h2>{{ 'hahaha' }}</h2>
    <h2>{{ 1+1 }}</h2>
    <h2>{{ {'name':'杨凡','age':18} }}</h2>
    <h2>{{ 1>2?'true':'false' }}</h2>
    <h2>{{ person.name }}</h2>
    <h2>{{ m2.split('').reverse().join('') }}</h2>

### 3、vue的指令系统 v-text v-html

new Vue({
        el: '#app',// 绑定需要操作的元素
        data() {
            return是必须要有的，可以没有返回的数据
            return {
                msg: '<h2>下班了</h2>'
            }
        }
    })

<div id="app">
    {{ msg }}
    <div v-text="msg"></div>
    <div v-html="msg"></div>
</div>
### 4、Vue的指令系统之 v-if和v-show

   (1)通过CSS样式进行显示和隐藏
   (2)通过dom操作删除增加来实现演示和隐藏

   v-if 真正的用于页面的渲染，因为它可以将页面的元素
        根据事件监听和子组件适当的增加和删除，惰性机制，初始值为false
        就不会进行渲染
   v-show 无论初值为为true还是false，都会将元素进行渲染，并且简单的基于
        CSS切换
   v-if 初始化开销低，v-show 初始化开销高
   频繁操作元素用v-show

### 5、Vue的指令系统之v-bind和v-on

v-bind可以绑定标签中的任何属性,缩写 :
v-on 可以监听 js中的所有事件,缩写 @

### 6、Vue的指令系统之v-for

​    可以遍历列表和对象的,使用v-for的时候一定要绑定key

    <ul v-if="data.status === 'ok'">
        <li v-for="(item,index) in data.users" :key="item.id">
            {{index}}--> {{item.id}} ---> {{item.name}}--->{{item.age}}
        </li>
    </ul>