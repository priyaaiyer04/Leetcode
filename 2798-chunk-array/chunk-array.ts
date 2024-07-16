type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
let i = 0;
let l1 = [];
let c = 0;
while (i < arr.length) {
    let l = arr.slice(i, i + size);
    l1.push(l);
    i += size;
}
return l1;
};
