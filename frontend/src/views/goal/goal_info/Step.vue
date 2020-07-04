<template>
  <div>
    <v-container fluid class="background">
    <v-row justify="center">
    <v-col cols="8">
    <div class="step">
    <div v-for="(step, index) in Steps.steps" :key="step.id">
       <!-- Use the v-for index to make the z-index descending. -->
        <div class="powerline" :style="zIndexAdjuster(index)">
        <div :class="isActiveRecColor(step.is_active)">
          {{ step.step_title }}
        </div>
        <div :class="isActiveTriColor(step.is_active)"></div>
      </div>
    </div>

   </div>
   </v-col>
   </v-row>
   </v-container>
  </div>
</template>

<script>
import api from "@/services/api";

export default{
  name: "Goal",
  props: ["Steps",],
  data: function(){
    return{
    }
  },
  methods: {
   // Change color of Step color depending on  `is_active` fields of Step Model.
    isActiveRecColor(is_active){
      if(is_active == true){
        return "rectangle-active rectangle";
      }
      if(is_active == false){
        return "rectangle-deactive rectangle";
      }
    },
   // Change color of Step color depending on  `is_active` fields of Step Model. 
   isActiveTriColor(is_active){
    if(is_active == true){
      return "triangle-active triangle";
    }
    if(is_active == false){
      return "triangle-deactive triangle";
    }
  },
  //  Use the v-for index to make the z-index descending.
   zIndexAdjuster(index){
    return `z-index: ${100 - index}`;
    },
  }

}
</script>


<style scoped>
.background {
  background: #f0f0f0;
}

.step {
  position: relative;
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  padding: 5px;
}

.powerline {
  display: inline-block;
  position: relative;
  filter: drop-shadow(0px 1px 1px rgba(70, 70, 70, 0.6));
  height: 100px;
}

.rectangle {
  width: 260px;
  height: 80px;
  display: inline-block;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  padding: 10px 0px 20px 60px;
  font-size: 18px;
}

/*  Change color of Step color depending on  `is_active` fields of Step Model. */
.rectangle-active{
  background: #4465c0;
  color: #f0f0f0;
}

.rectangle-deactive{
  background: #f0f0f0;
  color: rgb(43, 43, 43);
}

.triangle {
  border-top: 40px solid transparent;
  border-bottom: 40px solid transparent;
  display: inline-block;
  position: absolute;
}

/* Change color of Step color depending on  `is_active` fields of Step Model. */
.triangle-active{
  border-left: 50px solid #4465c0;
}

.triangle-deactive{
  border-left: 50px solid #f0f0f0;
}



::-webkit-scrollbar {
  display: none;
}
</style>
