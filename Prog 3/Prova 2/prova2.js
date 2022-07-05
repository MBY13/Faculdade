class Viagem {
	
	constructor() {
		this.km = 0.0;
		this.km_lt = 0.0;
		this.preco_lt = 0.0;
		this.vel = 0.0;
		this.litros = 0.0;
		this.custo = 0.0;
		this.tempo = 0.0;
	}
	
	get_Km(){
	    return(this.km);
	}
	
	get_Km_Lt(){
	    return(this.km_lt);
	}
	
	get_Preco_Lt(){
	    return(this.preco_lt);
	}
	
	get_Vel(){
	    return(this.vel)
	}
	
	get_Litros(){
	    return(this.litros);
	}
	
	get_Custo(){
	    return(this.custo);
	}
	
	get_Tempo(){
	    return(this.tempo);
	}
	
	//
	
	set_Km(km0){
	    this.km = km0;
	}
	
	set_Km_Lt(kmlt){
	    this.km_lt = kmlt;
	}
	
	set_Preco_Lt(pl){
	    this.preco_lt = pl;
	}
	
	set_Vel(vl){
	    this.vel = vl;
	}
	
	set_Litros(lt){
	    this.litros = lt;
	}
	
	set_Custo(cst){
	    this.custo = cst;
	}
	
	set_Tempo(tmp){
	    this.tempo = tmp;
	}
	
	calculo() {
	    var qtd_com = this.km / this.km_lt;
	    var custo_com = this.km / this.km_lt * this.preco_lt;
	    var tmp_viagem = this.km / this.vel;
	    
	    this.litros = qtd_com;
	    this.custo = custo_com;
	    this.tempo = tmp_viagem;
		// Questão 16:  (Crie o método que realiza os seguintes cálculos:
        //               a quantidade necessária de combustível,
        //               o custo desse combustível,
        //               o tempo de viagem)
	}
	
	toString() {
	    var Str = '';
	    Str += 'Quilometros: ' +this.km+ '\n';
	    Str += 'Km/Lt: ' +this.km_lt+ '\n';
	    Str += 'Preço/Lt: ' +this.preco_lt+ '\n';
	    Str += 'Velocidade: ' +this.vel+ '\n';
	    Str += '\n';
	    Str += 'Litros: ' +this.litros.toFixed(1)+ '\n';
	    Str += 'Custo/Viagem: ' +this.custo.toFixed(2)+ '\n';
	    Str += 'Tempo/Viagem: ' +this.tempo.toFixed(1)+ '\n';
	    
	    return(Str);
		// Questão 17: (Crie o método imprimir em uma string todas as
		//              características da classe Viagem)
	}
}

// ********************** //

function Limpar() {document.getElementById('id_km').value = '';
document.getElementById('id_km_lt').value = '';
document.getElementById('id_preco_lt').value = '';
document.getElementById('id_vel').value = '';
document.getElementById('id_litros').value = '';
document.getElementById('id_custo').value = '';
document.getElementById('id_tempo').value = '';
document.getElementById('id_console').value = '';
// Questão 18: (Construa uma função para limpar os formulários e o console na tela)
}

function Executar() {

var quilometros = document.getElementById('id_km').value;
var quilom_lt = document.getElementById('id_km_lt').value;
var prec_lit = document.getElementById('id_preco_lt').value;
var velo = document.getElementById('id_vel').value;
// Questão 19: (Extraia do formulário em tela todas as características da classe
//              Viagem e armazene em variáveis para posterior utilização)


let vi = new Viagem();
// Questão 20: (Aloque um objeto da classe Viagem)

vi.set_Km(quilometros);
vi.set_Km_Lt(quilom_lt);
vi.set_Preco_Lt(prec_lit);
vi.set_Vel(velo);
// Questão 21: (Insira no objeto todas as características da classe Viagem
//              recuperadas do formulário)

vi.calculo();
// Questão 22: (Chame o método que realiza todos os cálculos citados na Questão 16)

document.getElementById('id_litros').value = vi.get_Litros().toFixed(1);
document.getElementById('id_custo').value = vi.get_Custo().toFixed(2);
document.getElementById('id_tempo').value = vi.get_Tempo().toFixed(1);
// Questão 23: (Apresente o resultado dos cálculos nos componentes
//              identificados como: "id_litros", "id_custo" e "id_tempo")

document.getElementById('id_console').value = vi.toString();
// Questão 24: (Chame o método que escreve em uma string todas as características
//              da classe Viagem. Em seguida, imprima essa string no componente
//              identificado como: id_console)
}

// ********************** //