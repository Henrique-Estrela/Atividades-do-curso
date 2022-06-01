namespace forms
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {
            
        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged_1(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int dividendo = Convert.ToInt32(txtdividendo.Text);
            int divisor = Convert.ToInt32(txtdivisor.Text);
            int resto = dividendo % divisor;
            txtResto.Text = resto.ToString();

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void txtRestoDaDivisao3_TextChanged(object sender, EventArgs e)
        {

        }
    }
}