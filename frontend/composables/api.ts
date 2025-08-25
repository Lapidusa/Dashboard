import axios from 'axios'
import {listUrl} from "../src/utils/urlConfig";

export const useApi = () => {
  return axios.create({
    baseURL: listUrl.apiUrl as string
  })
}
