import Repository from "./Repository";

const resource = "/goals";
export default {
  get() {
    return Repository.get(`${resource}`);
  },

  getDetail(getId) {
    return Repository.get(`${resource}/${getId}`);
  },

  post(postId) {
    return Repository.post(`${resource}`, postId);
  },
  put(putId) {
    return Repository.put(`${resource}/${putId}`);
  },
  delete(deleteId) {
    return Repository.delete(`${resource}${deleteId}`);
  },
};
