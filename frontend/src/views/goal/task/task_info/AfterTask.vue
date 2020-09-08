<template>
  <div>
    <br />
    <br />
    <v-row justify="end">
    <v-btn fab small depressed color="gray" @click="switchEdit">
      <v-icon>mdi-pencil</v-icon>
    </v-btn>
    </v-row>
    
   <v-row>
   <v-col>
    <template v-if="TaskInfo.is_repeat">
     <v-chip
      color="gray"
    >
     <v-icon>loop</v-icon>Repeat
     
    </v-chip>

</template>
   </v-col>
   </v-row>

    <v-row>
      <v-col cols="12">
        <h1 class="message-title">{{ TaskInfo.task_title }}</h1>
      </v-col>
    </v-row>
    <br />

    <v-row>
      <v-col cols="12">
        <p class="writing-text">{{ TaskInfo.task_description }}</p>
      </v-col>
    </v-row>

    <br />
    <br />

    <v-row justify="center">
      <h2>Success criteria</h2>
    </v-row>

    <br />

    <v-row>
      <v-col cols="12">
        <p class="writing-text">{{ TaskInfo.criteria }}</p>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  name: "Task",
  props: ["TaskInfo"],

  methods: {
    switchEdit: function () {
      this.$emit("startEdit"); // <-  Control of parent method at `$emit`.
    }
  }
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            Font Desiign
 ------------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 40px;
  line-height: 40px;
  color: #088dda;
}

.category-title {
  font-size: 24px;
  /* text-align: center; */
  line-height: 30px;
  color: #292929;
}

.sub-title {
  font-size: 16px;
  /* text-align: center; */
  line-height: 30px;
  color: #292929;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  font-kerning: nomal;
  color: #292929;
  margin-block-end: 0em;
}
</style>
