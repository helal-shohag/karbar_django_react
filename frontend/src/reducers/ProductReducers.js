import { PRODUCT_LIST_REQUEST,PRODUCT_LIST_SUCCESS,PRODUCT_LIST_FAIL } from "../constants/productConstant"
export const productListReducers =(state = {Products : []},action) =>{
    switch(action.type){
        case PRODUCT_LIST_REQUEST:
            return {loading:true, Products:[]}
        case PRODUCT_LIST_SUCCESS:
            return {loading:false, Products:action.payload}
        case PRODUCT_LIST_FAIL:
            return {loading:false, error:action.payload}
        default:
            return state
    }
} 