const fastapi = async (operation, url, params, success_callback, failure_callback) => {

  let method = operation
  let content_type = 'application/json'
  let body = JSON.stringify(params)

  let _url = import.meta.env.VITE_SERVER_URL + url
  
  let options = {
    method: method,
    headers: {"Content-Type": content_type}
  }

  if (method === 'get') {
    _url += "?" + new URLSearchParams(params)
  } else {
    options['body'] = body
  }
  
  fetch(_url, options)
    .then(response => {
        if(response.status === 204) {  // No content
          if(success_callback) {
            success_callback()
          }
          return
        }
      response.json()
        .then(json => {
          if(response.status >= 200 && response.status < 300) {
            if(success_callback) {
              success_callback(json)
            }
          }else {
            if (failure_callback) {
              failure_callback(json)
            }else {
              alert(JSON.stringify(json))
            }
          }
        })
        .catch(error => {
          alert(JSON.stringify(error))
        })
    })
}

export default fastapi
