<template>
  <div class="q-pa-md" @click="sendMsg">
    <div class="q-gutter-y-md" style="max-width: 600px">
      <q-card>
        <q-tabs
          v-model="tab"
          dense
          class="bg-primary text-grey-7"
          active-color="primary"
          indicator-color="purple"
          align="justify"
        >
          <q-tab name="carton" label="动漫画" />
          <q-tab name="pix" label="像素画" />
          <q-tab name="char" label="字符画" />
        </q-tabs>

        <q-tab-panels v-model="tab" animated class="bg-primary text-white">
          <q-tab-panel name="carton">
            <q-form @submit="onSubmit" class="q-gutter-md">
            <div class="slide" style="float:left">
              <q-badge color="blue-4">
                动漫系数:小-->大
              </q-badge>
              <q-slider
              v-model="value"
              :min="1"
              :max="9"
              :step="2"
              label
              color="blue-4"
              />
              <div>
                <q-btn class="button1" label="确定" type="submit"></q-btn>
              </div>
            </div>
            </q-form>
            <q-img
              src="https://s2.loli.net/2021/12/10/uVzcQ6hWT1ZUdpO.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            <q-img
              src="https://s2.loli.net/2021/12/10/Uf4z6FQjgnIXMui.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
          </q-tab-panel>

          <q-tab-panel name="pix">
            <q-form @submit="onSubmit" class="q-gutter-md">
            <div class="slide" style="float:left">
              <q-badge color="blue-4">
                像素格尺寸:小-->大
              </q-badge>
              <q-slider
              v-model="value"
              :min="0.005"
              :max="0.05"
              :step="0.001"
              label
              color="blue-4"
              />
              <div>
                <q-btn class="button1" label="确定" type="submit"></q-btn>
              </div>
            </div>
            </q-form>
            <q-img
              src="https://s2.loli.net/2021/12/10/nkaiewZloN2TsUO.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            <q-img
              src="https://s2.loli.net/2021/12/10/t54n6sp9B1YRNSX.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
          </q-tab-panel>

          <q-tab-panel name="char">
            <q-form @submit="onSubmit" class="q-gutter-md">
            <div class="slide" style="float:left">
              <q-badge color="blue-4">
                字符密度:稀-->密
              </q-badge>
              <q-slider
              v-model="value"
              :min="4"
              :max="10"
              :step="0.1"
              label
              color="blue-4"
              />
              <div>
                <q-btn class="button1" label="确定" type="submit"></q-btn>
              </div>
            </div>
            </q-form>
            <q-img
              src="https://s2.loli.net/2021/12/10/nreHSTNWly3sOdj.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            <q-img
              src="https://s2.loli.net/2021/12/10/AINjhckVf7Rb19s.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </div>
  </div>
</template>

<script>
import submenu1Vue from './submenu1.vue'
export default {
  data () {
    return {
      tab: String,
      submitResult: "",
      value: String
    }
  },
  mounted(){
      this.tab;
      this.value;
  },
  methods:{
         sendMsg(){
             //func: 是父组件指定的传数据绑定的函数，this.msg:子组件给父组件传递的数据
             this.$emit('func',this.tab)
             this.$emit('size',this.value)
         },
         //onSubmit (evt) {
           // const formData = new FormData(evt.target)
            //const submitResult = ""

            //submitResult = this.value
            //console.log(this.value)

          //this.submitResult = submitResult
            //}
          }
}

</script>

<style>
.bg-primary {
    background:rgb(234,184,219) !important;
}
.q-tab-panel {
    padding: 30px;
}
.absolute-full, .fullscreen, .fixed-full {
    top: 0px;
    right: 4px;
    bottom: 0;
    left: 4px;
}
.slide{
  padding: 0px 20px;
  margin-top: 40px;
  width: 180px;
}
.button1{
  background-color:RGB(100,181,246);
}
</style>