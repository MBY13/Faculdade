class Roupa {
	
	constructor() {
	    this.id_km = '';
	    this.id_km_lt = '';
	    this.id_preco_lt = 0;
	    this.id_vel = 0;
	    this.id_litros = 0.0;
	    this.id_custo = 0.0;
		this.id_tempo = 0.0;
		this.id_console =0.0;	
	}
	
	get_Km() {
	    return(this.id_km);
	}
	
	get_Km_Lt() {
	    return(this.id_km_lt);
	}
	
	get_Preco_Lt() {
	    return(this.id_preco_lt);
	}
	
	get_Vel() {
	    return(this.id_vel);
	}
	
	get_Litros() {
	    return(this.id_litros);
	}
	
	get_Custo() {
	    return(this.id_custo);
	}

	get_Tempo() {
	    return(this.id_tempo);
	}
	
	//
	
	set_Km(mar) {
	    this.marca = mar;
	}
	
	set_Km_Lt(cor) {
	    this.cor = cor;
	}
	
	set_Preco_Lt(tam) {
	    this.tam = tam;
	}
	
	set_Vel(quant) {
	    this.quant = quant;
	}
	
	set_Litros(preco) {
	    this.preco = preco;
	}
	
	set_Custo(preco) {
	    this.preco = preco;
	}

	set_Tempo(preco) {
	    this.preco = preco;
	}
	
	toString() {
		var Str = '';
		Str += 'Marca: '+this.marca+'\n';
		Str += 'Cor: '+this.cor+'\n';
		Str += 'Tamanho: '+this.tam+'\n';
		Str += 'Quantidade: '+this.quant+'\n';
		Str += 'PreÃ§o: '+this.preco.toFixed(2)+'\n';
		Str += '\n';
		Str += 'Total: '+this.total.toFixed(2)+'\n';
		return(Str);
	}
}

// ************************************************************** //

function Limpar() {
	document.getElementById('id_marca').value = '';
	document.getElementById('id_cor').value = '';
	document.getElementById('id_tam').value = '';
	document.getElementById('id_quant').value = '';
	document.getElementById('id_preco').value = '';
	document.getElementById('id_total').value = '';
	document.getElementById('id_console').value = '';
}

function Executar() {
	var marca = document.getElementById('id_marca').value;
	var cor = document.getElementById('id_cor').value;
	var tam = parseInt(document.getElementById('id_tam').value);
	var quant = parseInt(document.getElementById('id_quant').value);
	var preco = parseFloat(document.getElementById('id_preco').value);
	
	let Rp = new Roupa();
	Rp.set_Marca(marca);
	Rp.set_Cor(cor);
	Rp.set_Tam(tam);
	Rp.set_Quant(quant);
	Rp.set_Preco(preco);
	Rp.calcula_Total();
	
	document.getElementById('id_total').value = Rp.get_Total().toFixed(2);
	
	document.getElementById('id_console').value = Rp.toString();
}
