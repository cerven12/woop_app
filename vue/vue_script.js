new Vue({
    el: '#app',
    data: {
        goals: {},
        new_goal: '',
    },
    mounted() {
        this.reloadGoal();
    },
    methods: {
        postGoal: function () {
            const vm = this;
            axios.post('http://127.0.0.1:8000/api/v1/Goal/',
                { title: this.new_goal })
                .then(response => { vm.reloadGoal(); })
        },
        deleteGoal: function (id) {
            const vm = this;
            axios.delete('http://127.0.0.1:8000/api/v1/Goal/' + id)
                .then(response => { vm.reloadGoal(); })
        },
        updataGoal: function (id) {
            const vm = this;
            axios.put('http://127.0.0.1:8000/api/v1/Goal/' + id,
                { title: this.input_title })
                .then(response => { vm.reloadGoal(); })
        },
        reloadGoal() {
            const vm = this;
            axios.get('http://127.0.0.1:8000/api/v1/Goal/')
                .then((response) => { vm.goals = response.data })
        }
    },
}
)