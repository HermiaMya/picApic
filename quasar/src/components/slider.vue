<template>
<div>
  <div style="display:inline; width:200px">
    <div class="q-pa-md" style="float:left; width:25%">
      <q-badge color="pink-3">
        灰度
      </q-badge>
      <q-slider
        v-model="value1"
        :max = "100"
        :min = "0"
        :step="1"
        label
        :label-value="value1 + '%'"
        color = "red-2"
      />
    </div>
    <div class="q-pa-md" style="float:left; width:25%">
      <q-badge color="pink-3">
        色相
      </q-badge>
      <q-slider
        v-model="value2"
        :max = "100"
        :min = "0"
        :step="1"
        label
        :label-value="value2 + '%'"
        color = "red-2"
      />
    </div>
    <div class="q-pa-md" style="float:right; width:25%">
      <q-badge color="pink-3">
        模糊度
      </q-badge>
      <q-slider
        v-model="value3"
        :max = "100"
        :min = "0"
        :step="1"
        label
        :label-value="value3 + '%'"
        color = "red-2"
      />
    </div>
    <div class="q-pa-md" style="float:right; width:25%">
      <q-badge color="pink-3">
        反转
      </q-badge>
      <q-slider
        v-model="value4"
        :max = "100"
        :min = "0"
        :step="1"
        label
        :label-value="value4 + '%'"
        color = "red-2"
      />
    </div>
  </div>

  <div style="display:inline; width:200px">
    <div class="q-pa-md" style="float:left; width:25%">
      <q-badge color="pink-3">
        亮度
      </q-badge>
      <q-slider
        v-model="value5"
        :max = "100"
        :min = "0"
        :step="1"
        label
        :label-value="value5 + '%'"
        color = "red-2"
      />
    </div>
    <div class="q-pa-md" style="float:left; width:25%">
      <q-badge color="pink-3">
        透明度
      </q-badge>
      <q-slider
        v-model="value6"
        :max = "100"
        :min = "0"
        :step="1"
        label
        :label-value="value6 + '%'"
        color = "red-2"
      />
    </div>
    <div class="q-pa-md" style="float:right; width:25%">
      <q-badge color="pink-3">
        对比度
      </q-badge>
      <q-slider
        v-model="value7"
        :max = "100"
        :min = "0"
        :step="1"
        label
        :label-value="value7 + '%'"
        color = "red-2"
      />
    </div>
    <div class="q-pa-md" style="float:right; width:25%">
      <q-badge color="pink-3">
        饱和度
      </q-badge>
      <q-slider
        v-model="value8"
        :max = "100"
        :min = "0"
        :step="1"
        label
        :label-value="value8 + '%'"
        color = "red-2"
      />
    </div>
  </div>
</div>
</template>

<script>
export default {
  data () {
    return {
      value1: 0,
      value2: 0,
      value3: 0,
      value4: 0,
      value5: 0,
      value6: 0,
      value7: 0,
      value8: 0
    }
  },
  method(){
    
  }
}
</script> 
<style>
.q-slider--h {
    width: 130%;
    height: 39px;
}

.q-pa-md {
    padding: 16px 50px;
}
</style>