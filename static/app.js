jQuery.ready(displayAllCupcakes())

async function displayAllCupcakes(){
    let url = "http://127.0.0.1:5000/api/cupcakes"
    all_cupcakes = await axios.get(url)

    for(let cupcake of all_cupcakes.data.cupcakes){
        let newCupcake = allListCupcakesTemplate(cupcake)
        $(".all_cupcakes").append(newCupcake)
    }
}


function allListCupcakesTemplate(cupcake_data){
    return `
    <div class="card col-3">
        <img src="${cupcake_data.image}" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">Flavor</h5>
            <p class="card-text">${cupcake_data.flavor}</p>
            <h5 class="card-title">Size</h5>
            <p class="card-text">${cupcake_data.size}</p>
            <h5 class="card-title">Rating</h5>
            <p class="card-text">${cupcake_data.rating}</p>
        </div>
    </div>
    `
}  


$("#add_cup_form").submit(handleFormSubmit)


async function handleFormSubmit(e){
    e.preventDefault()
    let url = "http://127.0.0.1:5000/api/cupcakes"
    await axios.post(url,{
        flavor:$("#flavor").val(),
        size:$("#size").val(),
        rating:$("#rating").val(),
        image:$("#image").val()
    })

    location.reload();
}


