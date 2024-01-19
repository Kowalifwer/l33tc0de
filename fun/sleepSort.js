const doAfter = (callable, time) => {
    return new Promise((resolve) =>{
        setTimeout(() => {
            callable()
            resolve()
        }, time)
    })
}

//in place kinda cap cuz u gotta store smelly coroutines/promises,
//i think in a language where you can just launch thread n then collect without storing somehow,
//this could be in place (idk tho lol)
// warning dont put elements too big
async function sleepSortInPlace(list) {
    let pos = 0
    let promises = []
    arr_size = list.length
    for (let elt of list) { // O(N)
        // launch process here.
        let time = elt * 3
        let promise = doAfter(() => {
            list[pos] = elt
            pos += 1
        }, time)
        promises.push(promise)
    }
    await Promise.all(promises)
    return list
}

(async () => {
    let res = await sleepSortInPlace([3,2,1,1,2,3,2,3,1,0,0,0,5,2,6,7,6,7,4,5,3,5,5,7,6,7,5,4,4])
    console.log(res)
})()