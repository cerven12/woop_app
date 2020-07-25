<template>
  <div>
    <div v-for="(worries, worries_index) in worryList" :key="worries_index">
      <div class="set">
        <input type='text' v-model="worries.worry" / >{{ worries_index }}
        <button @click="deleteWorryIdeaForm(worries_index)">✘</button><br />
        <div
          v-for="(ideas, ideas_index) in worries.ideaList"
          :key="ideas_index"
        >
          <input type='text' v-model="ideas.idea" class="right" / >{{
            ideas_index
          }}
          <button @click="deleteIdeaForm(worries_index, ideas_index)">✘</button
          ><br />
          <p><button @click="addIdeaForm(worries_index)">idea add</button></p>
        </div>
      </div>
    </div>
    {{ worryList.splice[(1, 1)] }}
    <div>
      <button @click="addWorryIdeaForm">addIdeaForm</button>
    </div>
    <pre>{{ $data }}</pre>
  </div>
</template>

<script>
  export default{
data: function(){
return {
   worryList: [
   { worry: "1", ideaList: [
     { idea: "1" }, // 1
     { idea: "2" }, // 2
     { idea: "3" }, // 3
     { idea: "4" }, // 4
     ] },
   { worry: "2", ideaList: [{ idea: "1" }] }, // 5
   { worry: "3", ideaList: [{ idea: "1" }] }, // 6
   { worry: "4", ideaList: [{ idea: "1" }] }  // 7
 ],
 };
  },
  methods: {
  	 addWorryIdeaForm: function() {
      const form = { worry: "", ideaList: [{ idea: "" }] };
      this.worryList.push(form);
    },
    addIdeaForm:function(worries_id){
      const form = {idea: ""};
      this.worryList[worries_id].ideaList.push(form)
    },
    deleteWorryIdeaForm:function(worry_id){
    	this.worryList.splice(worry_id, 1);
      console.log(this.worryList);
    },
     deleteIdeaForm:function(worries_id, ideas_id){
     this.worryList[worries_id].ideaList.splice(ideas_id, 1);
    },
  }
  }

</script>

<style scoped>
.set{
  border: solid 1px gray;
  padding: 10px;
  margin: 10px
}

.right{
  margin: 0 0 0 50px;
}
</style>
