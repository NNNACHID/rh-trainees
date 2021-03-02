<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

/*

function toTree(array $input,array $baseTable, $inputValue)
{
    if (count($input) == 0) {
        $returnValue = $inputValue;
    } else {
        $item = array_shift($input);
        if (isset($baseTable[$item])) {
            $baseTable[$item] = toTree($input, $baseTable[$item], $inputValue);
        } else {
            $baseTable[$item] = toTree($input, [], $inputValue);
        }
        $returnValue = $baseTable;
    }
    return $returnValue;
}


$inputs = [
    "b.d.e" => "blablabla",
    "b.a.e" => "blobloblo",
];
$tableauFinal = [];
foreach ($inputs as $inputKey => $inputValue) {
    $exploded = explode(".", $inputKey);
    $tableauFinal = toTree($exploded, $tableauFinal, $inputValue);
}
print_r($tableauFinal);

*/
