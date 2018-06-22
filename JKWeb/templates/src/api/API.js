//调用服务接口
import axios from 'axios'
import config from './config'

class API {

    //获取服务统一接口，各图表根据此接口自定义内容
    post(params) {

        return axios.post(params.paramUrl, params.paramRequest, config);
    };

    //优化后post请求
    myPost(url, params) {
        return new Promise((resolve, reject) => {
            axios.post(url, params, config).then(function (response) {
                // console.log("myPost中"+response);
                resolve(response.data)
            })
                .catch(function (err) {
                    reject(err)
                })
        })
    };

}

export default API;

