library ieee;
use     ieee.std_logic_1164.all;
use     ieee.numeric_std.all;

entity test is
port
  ( clk   : in  std_logic
  ; i     : in  unsigned(7 downto 0)

  ; o_reg : out unsigned(7 downto 0)
  ; o     : out unsigned(7 downto 0)
  );
end test;

architecture impl of test is
begin
    process(clk)
    begin
        if rising_edge(clk) then
            o_reg <= i;
        end if;
    end process;

    o <= i;
end impl;